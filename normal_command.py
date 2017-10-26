1. x.split(',') 分割字符串，按照括号中的分隔符
声明：s为字符串，rm为要删除的字符序列
s.strip(rm)
删除s字符串中开头、结尾处，位于
rm删除序列的字符
s.lstrip(rm)
删除s字符串中开头处，位于
rm删除序列的字符
s.rstrip(rm)
删除s字符串中结尾处，位于
rm删除序列的字符
注意：
(1).当rm为空时，默认删除空白符（包括
'\n', '\r', '\t', ' ')
(2).这里的rm删除序列是只要边（开头或结尾）上的字符在删除序列内，就删除掉。

2. github 使用常见问题
首次配置默认的用户名和Email地址信息等：
$git config user.name "your name"
$git config user.email "your email"
新建工程后，gpg设置问题
$git config -global gpg.program "C:\Program Files (x86)\GNU\GnuPG\gpg2.exe"
$git config user.signingkey 0FIOKS90(gpg密钥)

3. github使用步骤
(1)git init   #初始化一个项目，这个是新建一个文件夹，然后往cd /e:\文件名，进入文件夹，此文件夹则为工程文件夹
(2)git add  wenjianming.py      #别忘了后缀
(3)git commit -m "说明"
(4)git remote add origin git@github.com:pythonhan/learngit.git  #创建远程连接，origin为命名为origin，也可以改为别的
(5)git push origin master    #将本地上传内容推送到远程
(6)git push -u origin master #将本地上所有内容推送到远程库，适用于第一次push

4.从其他平台将代码同步到本地：
(1)在本地新建一个文件夹，在该文件夹下创建工程git init
(2)创建与远程库（需要下载的代码地址）的链接 git remote add origin git@github.com:pythonhan/learngit.git
(3)git clone git@github.com:pythonhan/learngit.git(项目地址)，此时本地就会有相关文件
(4)如果平台有更新， git pull origin master 即可完成更新


其他常用：
(1)git status  #查看当前文件夹
(2)git diff wenjianming.py  #查看文件前后版本差异
(3)git log    #显示从最近到最远的提交日志
(4)git reset --hard HEAD^       #回到上一版本，^表示上几个版本，^^^上面三个版本,或者HEAD改成commit id
(5)cat wenjianming.py   #查看文件内容
(6)git reflog   #记录每一次命令，找到commit id
(7)git checkout -- file #丢弃当前工作区的修改，回到最后一次git commit或者git add的状态
(8)git reset HEAD readme.txt  #可以把暂存区的修改撤销掉，重新放回工作区，即撤销add
(9)rm test.txt   #删除
(10)git clone git@github.com:pythonhan/practice.git  #将远程库克隆下来
(11)git checkout -b dev     #创建并切换到dev分支
(12)git branch dev   #创建dev分支
(13)git checkout dev    #切换dev分支
(14)git branch      #查看当前分支
(15)git merge dev       #将dev分支合并到master分支上,当前处于master分支下，运行此命令
(16)git branch -d dev       #删除dev分支
(17)git log --graph --pretty=oneline --abbrev-commit        #查看合并分支图，查看历史分支
(18)git merge --no-ff -m "注释"  dev     #表示合并时禁用fast forward,因为fast forward模式下删除分支后会丢掉分支信息，--no-ff可以使用普通模式合并，合并后的历史有分支
(19)git stash     #"储藏"当前工作现场，恢复现场后继续工作
(20)git stash apply     #恢复工作现场，但是不删除stash内容
(21)git stash drop  #删除工作现场
(22)git stash pop       #恢复的同时删除stash 内容
(23)git branch -D <NAME>        #<name>表示分支名，强力删除一个分支
(24)git remote    #查看远程库信息
(25)git remote -v   #查看远程库详细信息
(26)git push origin master/dev  #将后面指定的分支内容都push到远程库
(27)git checkout -b dev origin/dev   #创建远程origin/dev库分支到本地dev
(28)git pull   #把最新的提交从origin/dev抓下来在本地合并，解决冲突在推送
(29)git branch --set-upstream dev origin/dev    #指定本地dev库与远程origin/dev分支的连接
(30)git tag v1.0    #给当前分支加标签
(31)git tag     #查看所有标签
(32)git log --pretty=oneline --abbrev-commit    #查看历史提交的commit id
(33)git tag v0.9 commitid       #给某一id打标签
(34)git show <tagname>  #查看标签信息
(35)git tag -a  v0.1 -m "注释" id  #创建带有说明的标签
(36)git tag -d v0.1     #删除标签
(37)git push origin <tagname>   #推送标签到远程
(38)git push origin --tags      #一次性推送尚未推送到远程的所有本地标签
(39)git tag -d v0.9         #若要删除远程标签，应先从本地删除，然后再从远程删除
(40)git push origin :refs/tags/v0.9     #从远程删除
(41)git config --global color.ui true   #让git 显示颜色

其他相关：
国内git托管服务：码云（gitee.com）
先删除已有的github远程库，
git remote rm origin
关联码云远程库
git remote add origin(任意命名) git@gitee.com:...




4. cd ..   #返回上一层文件

