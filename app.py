<script>
    const firebaseConfig = { databaseURL: "https://cassiapromptv8-default-rtdb.firebaseio.com/" };
    firebase.initializeApp(firebaseConfig);
    const db = firebase.database();

    const urlParams = new URLSearchParams(window.location.search);
    const userId = urlParams.get('id'); // Pega o nome exatamente como está no link

    if (userId) {
        // Busca no Firebase se esse ID existe na pasta 'clientes'
        db.ref('clientes/' + userId).on('value', (snap) => {
            if (snap.exists()) {
                // Se existir (como a Helen_cristina que você criou), libera o app!
                document.getElementById('loader').style.display = 'none';
                document.getElementById('status-seguranca').innerText = "LICENÇA ATIVA: " + userId.toUpperCase();
            } else {
                // Se não existir, mostra a tela de bloqueio
                document.body.innerHTML = '<div style="background:#000;height:100vh;display:flex;align-items:center;justify-content:center;color:red;"><h1>🛡️ ACESSO REVOGADO</h1></div>';
            }
        });
    } else {
        document.body.innerHTML = '<div style="background:#000;height:100vh;"></div>';
    }
</script>
