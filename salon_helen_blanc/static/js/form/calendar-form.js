function selectedMonth(){
    let selectedId = document.getElementById("months").value;
    console.log('months -> ' + selectedId)
    window.location.href = 'calendar.html?month='+selectedId+'&year=2022'
}