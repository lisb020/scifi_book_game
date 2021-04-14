$('body').on('click', '.rate', function(event){
    let description = $("#description").val();
    alert(description);
    //trigger function to remove from database
    const url = "/send"

    fetch(url, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(description)
    });
});
