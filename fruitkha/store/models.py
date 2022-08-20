from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.email

    # if request.method == 'POST':
    #     form = NewsLetterForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    # else:
    #     form = NewsLetterForm()
