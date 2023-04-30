document.getElementById("predict-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const response = await fetch("/predict", {
        method: "POST",
        body: formData
    });

    const results = await response.json();
    document.getElementById("decision-tree-result").textContent = results.decision_tree;
    document.getElementById("linear-regression-result").textContent = results.linear_regression;
    document.getElementById("random-forest-result").textContent = results.random_forest;
});