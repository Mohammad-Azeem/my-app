npx create-react-app my-app
git commit -m "Initial commit" , git repo create my-app --public
git checkout -b update-logo
sed -i https://reactjs.org 's https://www.propelleraero.com/dirtmate/ g' 
sed -i '' 's|<img src="logo.svg"|<img src="https://www.propelleraero.com/wp-content/uploads/2021/05/Vector.svg"|g' index.html
git commit -m "update logo"
git add . , gh pr create --base master --head update_logo --title "Update Logo and Link"
gh pr merge <PR_NUMBER>


# REPO_URL https://github.com/Mohammad-Azeem/my-app.git


# Work from Blackbird Team
npx create-react-app base-react-app
cd base-react-app
gh auth login
gh repo create
git checkout -b update_logo
sed -i "" 's|img src={logo}|img src="https://www.propelleraero.com/wp-content/uploads/2021/05/Vector.svg"|g' src/App.js
sed -i "" 's|href="https://reactjs.org"|href="https://www.propelleraero.com/dirtmate/"|g' src/App.js
git add .
git commit -m "change logo and link"
git push origin update_logo
gh pr create --title "Update Logo" --body "Updating logo and link"
gh pr merge

# REPO_URL: https://github.com/chnerypersonal/base-react-app