export function buttonRedirect({ 
    buttonId, 
    endpoint,
}) {
    const button = document.getElementById(buttonId);
    const buttonDoesNotExist = !button

    if (buttonDoesNotExist) {
        return;
    }

    button.addEventListener("click", () => {
        window.location.href = endpoint;
    });
}
