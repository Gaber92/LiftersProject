
function vstaviRez() {
    var Ime = document.getElementById('Ime').value;
    var Poteg = document.getElementById('Poteg').value;
    var Sunek = document.getElementById('Sunek').value;
    var Biatlon = parseInt(Poteg) + parseInt(Sunek)
    
    var table = document.getElementById("Rezultati");

    var row = table.insertRow(table.rows.length);
    row.className = "tr"

    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    
    cell1.innerHTML = Ime;
    cell2.innerHTML = Poteg;
    cell3.innerHTML = Sunek;
    cell4.innerHTML = Biatlon;
    cell5.innerHTML = "<input type=\"button\" value=\"Izbrisi\"  class=\"buttonDodaj\" onclick=\"deleteTableRow(this)\" />"

    document.getElementById('Ime').value = ""
    document.getElementById('Poteg').value = ""
    document.getElementById('Sunek').value = ""
}

function deleteTableRow(button){
   var vrstica = button.parentElement.parentElement
   vrstica.remove(0)
}