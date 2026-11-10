
document.addEventListener("DOMContentLoaded", function () {

    // Edit comment elements
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");

    // Delete comment elements
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteForm = document.getElementById("deleteForm");
    const deleteModalElement = document.getElementById("deleteModal");

    // EDIT COMMENT
    for (let button of editButtons) {
        button.addEventListener("click", function (event) {
            event.preventDefault();

            const commentId = event.currentTarget.getAttribute("comment_id");
            const commentElement = document.getElementById(
                `comment${commentId}`
            );

            if (!commentElement || !commentText || !commentForm || !submitButton) {
                console.error("Edit comment elements could not be found.");
                return;
            }

            commentText.value = commentElement.innerText.trim();
            submitButton.innerText = "Update";

            commentForm.action = `edit_comment/${commentId}`;

            commentText.focus();
        });
    }

    // DELETE COMMENT
    for (let button of deleteButtons) {
        button.addEventListener("click", function (event) {
            event.preventDefault();

            const commentId = event.currentTarget.getAttribute("comment_id");

            if (!deleteForm || !deleteModalElement) {
                console.error("Delete form or modal could not be found.");
                return;
            }

            deleteForm.action = `delete_comment/${commentId}`;

            if (typeof bootstrap === "undefined") {
                console.error("Bootstrap JavaScript is not loaded.");
                return;
            }

            const deleteModal = bootstrap.Modal.getOrCreateInstance(
                deleteModalElement
            );

            deleteModal.show();
        });
    }

});
