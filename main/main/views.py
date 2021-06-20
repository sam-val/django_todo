
from django.http.response import HttpResponseRedirect

from django.urls import reverse
from django.contrib.auth import login as l
from django.contrib.auth import logout as lo


# def login(r):
#     if r.user.is_authenticated:
#         return HttpResponseRedirect(reverse('todolist:index')) 
#     else:
#         l(r, r.user)

# def logout(r):
#     lo(r)
#     return HttpResponseRedirect(reverse('todolist:index'))

# def reset_pass(r):
#     pass