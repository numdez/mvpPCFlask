function deleteNote(noteId){
    fetch('/delete-note',{
        method:'POST',
        body: JSON.stringify({ noteId: noteId})
    }).then((_res) => {
        window.location.href = "/";
    });
}

function moveNote(noteId){
    fetch('/move-note', {
        method:'POST',
        body: JSON.stringify({noteId: noteId})
    }).then((_res) => {
        window.location.href='/';
    });
}