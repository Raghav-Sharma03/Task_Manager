import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  const fetchTasks = async () => {
    const res = await axios.get("http://127.0.0.1:5000/tasks");
    setTasks(res.data);
  };

  const addTask = async () => {
    if (!title) return;
    await axios.post("http://127.0.0.1:5000/tasks", { title });
    setTitle("");
    fetchTasks();
  };

  const deleteTask = async (id) => {
    await axios.delete(`http://127.0.0.1:5000/tasks/${id}`);
    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div style={{ 
      maxWidth: "500px", 
      margin: "50px auto", 
      textAlign: "center",
      fontFamily: "Arial"
    }}>
      <h1>📝 Task Manager</h1>

      <div style={{ marginBottom: "20px" }}>
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Enter task..."
          style={{ padding: "10px", width: "70%" }}
        />
        <button 
          onClick={addTask}
          style={{ padding: "10px", marginLeft: "10px" }}
        >
          Add
        </button>
      </div>

      <ul style={{ listStyle: "none", padding: 0 }}>
        {tasks.map((t) => (
          <li key={t.id} style={{
            background: "#f5f5f5",
            margin: "10px 0",
            padding: "10px",
            display: "flex",
            justifyContent: "space-between"
          }}>
            <span>{t.title}</span>
            <button onClick={() => deleteTask(t.id)}>❌</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;