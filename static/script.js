const API_ENDPOINTS = {
    get: "/users",
    post: "/users",
    put: "/users",
    patch: "/users",
    delete: "/users"
};

// ========================================
// Универсальный запрос
// ========================================

async function request(url, options, outputId, statusId) {
    const output = document.getElementById(outputId);
    const status = document.getElementById(statusId);

    output.textContent = "Отправка запроса...";
    status.textContent = "";

    try {
        const response = await fetch(url, options);
        const text = await response.text();

        let data;

        try {
            data = text
                ? JSON.parse(text)
                : "Пустой ответ";
        } catch {
            data = text;
        }

        status.textContent = `HTTP ${response.status}`;

        if (typeof data === "string") {
            output.textContent = data;
        } else {
            output.textContent = JSON.stringify(
                data,
                null,
                2
            );
        }
    } catch (error) {
        console.error(error);

        status.textContent = "ERROR";
        output.textContent =
            `Ошибка запроса:\n${error.message}`;
    }
}

// ========================================
// GET /users/:id
// ========================================

function getUser() {
    const id = document.getElementById("getId").value.trim();

    if (!id) {
        document.getElementById("getStatus").textContent = "ERROR";
        document.getElementById("getOutput").textContent =
            "Укажи ID пользователя.";
        return;
    }

    request(
        `${API_ENDPOINTS.get}/${encodeURIComponent(id)}`,
        {
            method: "GET"
        },
        "getOutput",
        "getStatus"
    );
}

// ========================================
// POST /users
// ========================================

function postUser() {
    const firstName =
        document.getElementById("postFirstName").value.trim();

    const lastName =
        document.getElementById("postLastName").value.trim();

    const age =
        document.getElementById("postAge").value;

    if (!firstName || !lastName || !age) {
        document.getElementById("postStatus").textContent = "ERROR";
        document.getElementById("postOutput").textContent =
            "Заполни все поля.";
        return;
    }

    const body = {
        first_name: firstName,
        last_name: lastName,
        age: Number(age)
    };

    request(
        API_ENDPOINTS.post,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(body)
        },
        "postOutput",
        "postStatus"
    );
}

// ========================================
// PUT /users/:id
// ========================================

function putUser() {
    const id =
        document.getElementById("putId").value.trim();

    const firstName =
        document.getElementById("putFirstName").value.trim();

    const lastName =
        document.getElementById("putLastName").value.trim();

    const age =
        document.getElementById("putAge").value;

    if (!id) {
        document.getElementById("putStatus").textContent = "ERROR";
        document.getElementById("putOutput").textContent =
            "Укажи ID пользователя.";
        return;
    }

    if (!firstName || !lastName || !age) {
        document.getElementById("putStatus").textContent = "ERROR";
        document.getElementById("putOutput").textContent =
            "Заполни все поля.";
        return;
    }

    const body = {
        first_name: firstName,
        last_name: lastName,
        age: Number(age)
    };

    request(
        `${API_ENDPOINTS.put}/${encodeURIComponent(id)}`,
        {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(body)
        },
        "putOutput",
        "putStatus"
    );
}


// ========================================
// PATCH /users/:id
// ========================================

function patchUser() {
    const id =
        document.getElementById("patchId").value.trim();

    const firstName =
        document.getElementById("patchFirstName").value.trim();

    const lastName =
        document.getElementById("patchLastName").value.trim();

    const age =
        document.getElementById("patchAge").value;

    if (!id) {
        document.getElementById("patchStatus").textContent = "ERROR";
        document.getElementById("patchOutput").textContent =
            "Укажи ID пользователя.";
        return;
    }

    const body = {};

    // PATCH отправляет только заполненные поля.
    if (firstName) {
        body.first_name = firstName;
    }

    if (lastName) {
        body.last_name = lastName;
    }

    if (age !== "") {
        body.age = Number(age);
    }

    if (Object.keys(body).length === 0) {
        document.getElementById("patchStatus").textContent = "ERROR";
        document.getElementById("patchOutput").textContent =
            "Измени хотя бы одно поле.";
        return;
    }

    request(
        `${API_ENDPOINTS.patch}/${encodeURIComponent(id)}`,
        {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(body)
        },
        "patchOutput",
        "patchStatus"
    );
}

// ========================================
// DELETE /users/:id
// ========================================

function deleteUser() {
    const id =
        document.getElementById("deleteId").value.trim();

    if (!id) {
        document.getElementById("deleteStatus").textContent = "ERROR";
        document.getElementById("deleteOutput").textContent =
            "Укажи ID пользователя.";
        return;
    }

    request(
        `${API_ENDPOINTS.delete}/${encodeURIComponent(id)}`,
        {
            method: "DELETE"
        },
        "deleteOutput",
        "deleteStatus"
    );
}