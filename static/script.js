async function fetchTasks() {
    try {
        const response = await fetch('/tasks');
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const tasks = await response.json();
        createTasks(tasks);
        updateTotalTime(tasks);
    } catch (error) {
        console.error("Error fetching tasks:", error);
        alert(`Error fetching tasks: ${error.message}`);
    }
}

function createTasks(tasks) {
    const taskContainer = document.querySelector('.task-container');
    taskContainer.innerHTML = '';  // Önce eski içerikleri temizleyelim.

    tasks.forEach(task => {
        const card = document.createElement('div');
        card.classList.add('card', 'col-md-4', 'p-2');

        const img = document.createElement('img');
        img.src = task.image;
        img.classList.add('card-img-top');
        card.appendChild(img);

        const cardBody = document.createElement('div');
        cardBody.classList.add('card-body');

        const title = document.createElement('h5');
        title.textContent = `${task.order}. ${task.content}`;
        cardBody.appendChild(title);

        const time = document.createElement('p');
        time.textContent = `Time: ${task.time} min`;
        cardBody.appendChild(time);

        if (task.chef_required) {
            const chefIcon = document.createElement('p');
            chefIcon.innerHTML = '👨‍🍳 Chef Required';
            cardBody.appendChild(chefIcon);
        }

        const inputContainer = document.createElement('div');
        inputContainer.classList.add('input-container');

        const inputLabel = document.createElement('label');
        inputLabel.textContent = "Start Time:";
        inputContainer.appendChild(inputLabel);

        const input = document.createElement('input');
        input.type = 'number';
        input.min = 0;
        input.max = 300;
        input.value = task.order * 10;  // Başlangıç değeri
        input.name = task.id;
        input.classList.add('form-control');
        input.addEventListener('input', () => updateTotalTime(tasks));
        inputContainer.appendChild(input);

        cardBody.appendChild(inputContainer);
        card.appendChild(cardBody);
        taskContainer.appendChild(card);
    });
}

function updateTotalTime(tasks) {
    const alertContainer = document.getElementById('alert-container');
    alertContainer.innerHTML = '';  // Eski uyarıları temizle.

    let totalTime = 0;
    let valid = true;

    tasks.forEach(task => {
        const input = document.querySelector(`input[name="${task.id}"]`);
        if (!input) {
            console.error(`Input not found for task: ${task.id}`);
            return;
        }
        const startTime = parseInt(input.value) || 0;
        const endTime = startTime + task.time;

        task.start = startTime;
        task.end = endTime;

        task.prerequisites.forEach(prereqId => {
            const prereqTask = tasks.find(t => t.id === prereqId);
            if (prereqTask && prereqTask.end > task.start) {
                const alert = document.createElement('div');
                alert.classList.add('alert', 'alert-danger');
                alert.textContent = `Prerequisites of "${task.content}" are not met!`;
                alertContainer.appendChild(alert);
                valid = false;
            }
        });

        totalTime = Math.max(totalTime, endTime);
    });

    if (valid) {
        document.getElementById('total-time').textContent = `Total Time: ${totalTime} min`;
    }
}

document.addEventListener('DOMContentLoaded', fetchTasks);
