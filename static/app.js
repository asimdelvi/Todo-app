const binButton = document.querySelectorAll('.bin');
const listGroup = document.querySelectorAll('.list-group-item');

binButton.forEach(button => button.style.visibility ="hidden");

for (let i = 0; i < listGroup.length; i++) {
  listGroup[i].addEventListener('mouseover', () => {
    binButton[i].style.visibility = 'visible';
  })

  listGroup[i].addEventListener('mouseout', () => {
    binButton[i].style.visibility = 'hidden';
  })
}

