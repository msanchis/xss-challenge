echo "# xss-challenge" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:msanchis/xss-challenge.git
git push -u origin main
