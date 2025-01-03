import hmac
import hashlib
import subprocess
from django.http import HttpResponse, HttpResponseForbidden
from decouple import config

GITHUB_SECRET = config('GITHUB_SECRET_WEBHOOK')

def github_webhook(request):
    if request.method != "POST":
        return HttpResponseForbidden("Invalid method")

    # Validate the signature
    header_signature = request.headers.get("X-Hub-Signature-256")
    if not header_signature:
        return HttpResponseForbidden("Missing signature")

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha256':
        return HttpResponseForbidden("Invalid signature method")

    mac = hmac.new(
        GITHUB_SECRET.encode(),
        msg=request.body,
        digestmod=hashlib.sha256
    )
    if not hmac.compare_digest(mac.hexdigest(), signature):
        return HttpResponseForbidden("Signature mismatch")

    # Pull latest changes and restart the application
    try:
        subprocess.run(['git', 'pull'], cwd='/home/prachigore/portfolio_api', check=True)
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], cwd='/home/prachigore/portfolio_api', check=True)
        subprocess.run(['python', 'manage.py', 'makemigrations'], cwd='/home/prachigore/portfolio_api', check=True)
        subprocess.run(['python', 'manage.py', 'migrate'], cwd='/home/prachigore/portfolio_api', check=True)
        subprocess.run(['python', 'manage.py', 'collectstatic', '--noinput'], cwd='/home/prachigore/portfolio_api', check=True)
        subprocess.run(['touch', '/var/www/prachigore_pythonanywhere_com_wsgi.py'], check=True)
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Deployment failed: {str(e)}", status=500)

    return HttpResponse("Deployed successfully!", status=200)
