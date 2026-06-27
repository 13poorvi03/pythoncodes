let expensesList = [];

function showSection(id) {
  document.querySelectorAll('.section').forEach(sec => sec.classList.add('hidden'));
  document.getElementById(id).classList.remove('hidden');
}

// Add Expense
document.getElementById("expenseForm").addEventListener("submit", function(e) {
  e.preventDefault();

  let date = document.getElementById("date").value;
  let category = document.getElementById("category").value;
  let description = document.getElementById("description").value;
  let amount = parseFloat(document.getElementById("amount").value);

  let expense = { date, category, description, amount };
  expensesList.push(expense);

  document.getElementById("msg").innerText = "✅ Expense added successfully!";
  this.reset();
});

// View All Expenses
function renderExpenses() {
  let list = document.getElementById("expenseList");
  list.innerHTML = "";
  if (expensesList.length === 0) {
    list.innerHTML = "<li>No Expenses Added. Bro spend some moneyy 😅</li>";
  } else {
    expensesList.forEach((exp, index) => {
      list.innerHTML += `<li>${index+1}. ${exp.date} | ${exp.category} | ${exp.description} | ₹${exp.amount}</li>`;
    });
  }
}
document.querySelector("button[onclick=\"showSection('view')\"]").addEventListener("click", renderExpenses);

// View Total Spending
function renderTotal() {
  let total = expensesList.reduce((sum, exp) => sum + exp.amount, 0);
  document.getElementById("totalAmount").innerText = "₹" + total;
}
document.querySelector("button[onclick=\"showSection('total')\"]").addEventListener("click", renderTotal);
