function check() {
    if (document.getElementById("name").value != "" && document.getElementById("mail").value != ""){
        document.getElementById("name").value = "Успешно";
        document.getElementById("mail").value = "отправлено";
        document.getElementById("name").disabled = true;
        document.getElementById("mail").disabled = true;
        document.getElementById("Send").setAttribute('disabled', true);
    } else{
        console.log("Пусто");
    }
}
