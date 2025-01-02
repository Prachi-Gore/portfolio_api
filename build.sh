set -o errexit # exit on error

echo "Installing dependencies..."
pip install -r requirements.txt

# python manage.py collectstatic --no-input

echo "Applying database migrations..."
python manage.py migrate


echo "Deployment completed successfully."
