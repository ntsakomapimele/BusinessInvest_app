function createPost() {
    const content = document.getElementById("postContent").value;
    if (content.trim() === "") {
        alert("Please write something to post.");
        return;
    }

    const postTemplate = `
        <div class="post">
            <h6 class="text-primary">You</h6>
            <p>${content}</p>
            <div class="post-actions d-flex justify-content-between align-items-center">
                <button class="btn btn-like btn-sm" onclick="likePost(this)">
                    <i class="bi bi-hand-thumbs-up"></i> Like (<span class="like-count">0</span>)
                </button>
                <button class="btn btn-show-comments btn-sm" onclick="toggleComments(this)">
                    <i class="bi bi-chat-dots"></i> Show Comments
                </button>
                <button class="btn btn-danger btn-sm" onclick="deletePost(this)">
                    <i class="bi bi-trash"></i> Delete
                </button>
                <div class="social-icons">
                    <a href="#" title="Share on WhatsApp"><i class="bi bi-whatsapp"></i></a>
                    <a href="#" title="Share on Facebook"><i class="bi bi-facebook"></i></a>
                    
                </div>
            </div>
            <div class="comments-section mt-3" style="display: none;">
                <textarea class="form-control mb-2 comment-input" placeholder="Write a comment..."></textarea>
                <button class="btn btn-primary btn-sm" onclick="postComment(this)">Post Comment</button>
                <ul class="list-unstyled mt-2 comments-list"></ul>
            </div>
        </div>
    `;
    document.getElementById("postsFeed").insertAdjacentHTML("afterbegin", postTemplate);
    document.getElementById("postContent").value = "";
}

function toggleComments(button) {
    const commentSection = button.parentElement.nextElementSibling;
    const isVisible = commentSection.style.display === "block";
    commentSection.style.display = isVisible ? "none" : "block";
    button.innerHTML = `<i class="bi bi-chat-dots"></i> ${isVisible ? "Show Comments" : "Hide Comments"}`;
}
function shareOnFacebook() {
    const url = encodeURIComponent(window.location.href); // Encode the current URL
    const facebookUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`; // Construct the Facebook sharing URL
    window.open(facebookUrl, '_blank'); // Open the link in a new tab
}

function shareOnWhatsApp() {
    const url = encodeURIComponent(window.location.href); // Encode the current URL
    const text = encodeURIComponent("Check out this page: "); // Optional text to share
    const whatsappUrl = `https://wa.me/?text=${text}${url}`; // Construct the WhatsApp sharing URL
    window.open(whatsappUrl, '_blank'); // Open the link in a new tab
}

function likePost(button) {
    const likeCount = button.querySelector(".like-count");
    let count = parseInt(likeCount.innerText);
    likeCount.innerText = ++count;
}

function deletePost(button) {
    const post = button.closest(".post");
    post.remove();
}

function postComment(button) {
    const commentInput = button.previousElementSibling;
    const commentText = commentInput.value.trim();
    if (commentText === "") {
        alert("Please enter a comment.");
        return;
    }

    const commentList = button.nextElementSibling;
    const newComment = `<li><strong>You:</strong> ${commentText}</li>`;
    commentList.insertAdjacentHTML("beforeend", newComment);
    commentInput.value = ""; // Clear the input after posting
}
