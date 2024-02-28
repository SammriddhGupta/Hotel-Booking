the folder needs to be placed in Macintosh HD/opt/homebrew/var/www/ and there, the www folder probably already has cg-bin and index.html file, don't touch them unless you know why

easy way to install apache tomcat is `brew install httpd`
[yt link here](https://www.youtube.com/watch?v=xyHlJLjzf1w)

start server with command `brew services start httpd`

restart with `brew services restart httpd`

stop with `brew services stop httpd`

install aws-cli via their website command

aws amplify docs to setup a real nice React based auth login page, [link](https://docs.amplify.aws/javascript/build-a-backend/auth/set-up-auth/)

Good debugging [ref](https://stackoverflow.com/questions/76888416/getting-error-message-error-description-invalid-scope-when-trying-to-authentica)