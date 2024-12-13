document.addEventListener('DOMContentLoaded', function() {
    var currentQuestion = 1;
    var totalQuestions = document.querySelectorAll('.question').length;
    var points = 0; // Initialize point counter

    function showQuestion(questionNumber) {
        document.querySelectorAll('.question').forEach(function(question, index) {
            question.style.display = (index + 1 === questionNumber) ? 'block' : 'none';
        });
    }

    function updatePoints() {
        console.log('Updating points display:', points);
        document.getElementById('points').textContent = 'Points: ' + points;
    }

    function displayFinalScore() {
        var quizContent = document.querySelector('.quiz-content');
        quizContent.innerHTML = `
            <div class="final-score-container">
                <h2>Well done!🥳🥳🥳</h2>
                <p>🎉🎊You have completed the quiz.🎉🎊</p>
                <p>Your final score is: ${points} points.</p>
            </div>
        `;
    }

    document.getElementById('next').addEventListener('click', function() {
        if (currentQuestion < totalQuestions) {
            currentQuestion++;
            showQuestion(currentQuestion);
        } else if (currentQuestion === totalQuestions) {
            displayFinalScore();
        }
    });

    document.getElementById('prev').addEventListener('click', function() {
        if (currentQuestion > 1) {
            currentQuestion--;
            showQuestion(currentQuestion);
        }
    });

    document.querySelectorAll('.option').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            var selectedOption = event.target;
            var selectedOptionValue = selectedOption.value;
            var questionId = selectedOption.closest('form').querySelector('[name="question_id"]').value;
            var resultMessageDiv = selectedOption.closest('.question').querySelector('.result-message');
            var buttons = selectedOption.closest('.options').querySelectorAll('.option');

            fetch('/game/check_answer/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify({ option: selectedOptionValue, question_id: questionId })
            })
            .then(response => response.json())
            .then(data => {
                resultMessageDiv.innerHTML = data.result;
                buttons.forEach(btn => {
                    btn.disabled = true;
                    if (btn.value === selectedOptionValue) {
                        if (data.correct) {
                            btn.classList.add('correct');
                            points+=10; // Increment points for correct answer
                            console.log('Correct answer. Points:', points);
                            updatePoints(); // Update the points display
                        } else {
                            btn.classList.add('incorrect');
                        }
                    } else if (!data.correct && btn.value === data.correct_answer) {
                        btn.classList.add('correct');
                    }
                });
            })
            .catch(error => console.error('Error:', error));
        });
    });

    showQuestion(currentQuestion);
    updatePoints(); // Initialize points display
});
