import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        // Busca os cursos lá do seu app.py
        axios.get("http://localhost:8001/api/courses")
            .then(res => setCourses(res.data))
            .catch(err => console.log("Erro ao carregar cursos"));
    }, []);

    return (
        <div className="p-8">
            <h1 className="text-3xl font-bold mb-6 photo-accent">Cássia Prompt - V8 God Mode</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {courses.map(course => (
                    <div key={course.id} className="border border-zinc-700 p-4 rounded-lg bg-zinc-900">
                        <img src={course.image_url} alt={course.title} className="rounded mb-2" />
                        <h2 className="text-xl font-bold ai-accent">{course.title}</h2>
                        <button className="mt-4 btn-primary">Acessar Curso</button>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Dashboard;

