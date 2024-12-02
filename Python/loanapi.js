const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');
const moment = require('moment'); // Подключаем библиотеку moment

const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Подключение к базе данных
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '', // Замените на ваш пароль
    database: 'test'    // Замените на вашу базу данных
});

db.connect((err) => {
    if (err) {
        console.error('Ошибка подключения к базе данных:', err);
        return;
    }
    console.log('Подключено к базе данных MySQL');
});

// Эндпоинт для получения всех клиентов
app.get('/api/clients', (_, res) => {
    db.query('SELECT * FROM clients', (err, results) => {
        if (err) {
            res.status(500).json({ error: 'Ошибка выполнения запроса' });
        } else {
            // Преобразуем даты в нужный формат
            const transformedData = results.map(client => {
                return {
                    ...client,
                    start_date: moment(client.start_date).format('YYYY-MM-DD'),  // Преобразуем дату
                    end_date: moment(client.end_date).format('YYYY-MM-DD')      // Преобразуем дату
                };
            });

            res.json({
                success: true,
                data: transformedData
            });
        }
    });
});

// Эндпоинт для получения всех типов
app.get('/api/types', (_, res) => {
    db.query('SELECT * FROM types', (err, results) => {
        if (err) {
            res.status(500).json({ error: 'Ошибка выполнения запроса' });
        } else {
            res.json({
                success: true,
                data: results
            });
        }
    });
});

app.get('/api/types/names', (_, res) => {
    db.query('SELECT type FROM types', (err, results) => {
        if (err) {
            res.status(500).json({ error: 'Ошибка выполнения запроса' });
        } else {
            res.json({
                success: true,
                data: results
            });
        }
    });
});

app.get('/api/clients/names', (_, res) => {
    db.query('SELECT name FROM clients', (err, results) => {
        if (err) {
            res.status(500).json({ error: 'Ошибка выполнения запроса' });
        } else {
            res.json({
                success: true,
                data: results
            });
        }
    });
});

// Эндпоинт для удаления клиента по ID
app.delete('/api/clients/:id', (req, res) => {
    const clientId = req.params.id;

    // Проверяем, что ID передан и является числом
    if (!clientId || isNaN(clientId)) {
        return res.status(400).json({ error: 'Некорректный ID клиента' });
    }

    // SQL-запрос на удаление клиента
    const query = 'DELETE FROM clients WHERE id = ?';

    db.query(query, [clientId], (err, results) => {
        if (err) {
            console.error('Ошибка выполнения запроса:', err);
            return res.status(500).json({ error: 'Ошибка выполнения запроса' });
        }

        // Проверяем, были ли удалены строки
        if (results.affectedRows === 0) {
            return res.status(404).json({ error: 'Клиент с указанным ID не найден' });
        }

        res.json({
            success: true,
        });
    });
});


// Запуск сервера
app.listen(port, () => {
    console.log(`Сервер запущен на http://localhost:${port}`);
});