function deleteTodo(task_id) {
    if (!confirm(`Are you sure you want to delete task #${task_id}?`)) {
        return;
    }

    fetch(`/remove_todo/${task_id}`, {  // ✅ Only task_id in URL
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        // ✅ Always check if response is OK before .json()
        if (!response.ok) {
            return response.json().then(err => { throw err; });
        }
        return response.json();
    })
    .then(data => {
        // ✅ Now data.message or data.error will be defined
        alert(data.message || data.error);
        if (data.message) {
            const element = document.querySelector(`[data-task-id="${task_id}"]`);
            if (element) element.remove();
        }
    })
    .catch(err => {
        console.error("Delete failed:", err);
        alert("Failed to delete task. Check console for details.");
    });
}