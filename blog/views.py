
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

            messages.success(
                request,
                "Comment submitted and awaiting approval"
            )

            return HttpResponseRedirect(
                reverse("post_detail", args=[slug])
            )
    else:
        comment_form = CommentForm()

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "coder": "Matt Rudge",
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


@login_required
@require_POST
def comment_edit(request, slug, comment_id):
    post = get_object_or_404(
        Post,
        slug=slug,
        status=1
    )

    comment = get_object_or_404(
        Comment,
        pk=comment_id,
        post=post
    )

    if comment.author == request.user:
        comment_form = CommentForm(
            data=request.POST,
            instance=comment
        )

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.approved = False
            comment.save()

            messages.success(request, "Comment Updated!")
        else:
            messages.error(request, "Error updating comment!")
    else:
        messages.error(
            request,
            "You can only edit your own comments!"
        )

    return HttpResponseRedirect(
        reverse("post_detail", args=[slug])
    )


@login_required
@require_POST
def comment_delete(request, slug, comment_id):
    post = get_object_or_404(
        Post,
        slug=slug,
        status=1
    )

    comment = get_object_or_404(
        Comment,
        pk=comment_id,
        post=post
    )

    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Comment deleted!")
    else:
        messages.error(
            request,
            "You can only delete your own comments!"
        )

    return HttpResponseRedirect(
        reverse("post_detail", args=[slug])
    )
