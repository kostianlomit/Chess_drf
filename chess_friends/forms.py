
from time import sleep
from django.core.mail import send_mail
from django import forms
from chess_friends.tasks import send_feedback_email_task
class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        """Sends an email when the feedback form has been submitted."""
        sleep(20)  # Simulate expensive operation(s) that freeze Django
        send_mail(
            "Your Feedback",
            f"\t{self.cleaned_data['message']}\n\nThank you!",
            "support@example.com",
            [self.cleaned_data["email_address"]],
            fail_silently=False,
        )

    # def send_email(self):
    #     send_feedback_email_task.delay(
    #         self.cleaned_data["email"], self.cleaned_data["message"]
    #     )