<h1>TOJHelper : V.0.6</h1>
<h3>Under Testing</h3>
A batch-testing sublime plug-in for Timus Online Judge
<br><br>
This application is to assist a competitive-programmer while practicing on TOJ. This application downloads all the sample test cases for a problem and runs a user&#39;s solution program on all these test cases so that no time is wasted on manual checking of the solution and then directly submits the solution to TOJ without leaving the editor.

For now the application is for C++ users only.
<br>
<br>
<b>Make Sure you have read the <a href="#installation">Installation</a> and <a href="#usage">Usage</a> very very carefully.</b>
<br>

<h3>Index</h3>
<ol>
<li><a href="#requisites">Requisites</a></li>
<li><a href="#installation">Installation</a></li>
<li><a href="#usage">Usage</a></li>
<li><a href="#techused">Technology Used</a></li>
<li><a href="#testing">Testing</a></li>
<li><a href="#contributors">Contrubutors</a></li>
<li><a href="http://bugecode.com/post.php?pid=121" target="_blank">FAQ</a></li>
</ol>

<a name="requisites"><h3>Requisites</h3></a>
<ul>
<li>Linux (Tested on Ubuntu-14.04)</li>
<li>Internet Connection (it should be working on terminal)</li>
<li>Sublime Text-3
	<ul>
	<li>To check Sublime is installed correctly
		<ol>
		<li>Open a <b>terminal</b> window.</li>
		<li>Run "subl".</li>
		<li>If Sublime opens up, everything is perfect.</li>
		</ol>
	</li>
	</ul>	
</li>
<li>A default browser</li>
<li>Working g++
	<ul>
	<li>To check g++ is working
		<ol>
		<li>Open a <b>terminal</b> window.</li>
		<li>Run "g++".</li>
		<li>If it identifies the command, everything is perfect.</li>
		</ol>
	</li>
	</ul>
</li>
<li>Python libraries
	<ul>
	<li>mechanize</li>
	<li>bs4 (BeautifulSoup)</li>
	<li></li>
	</ul>
</li>
</ul>

<a name="installation"><h3>Installation</h3></a>
<ol>
<li>Make sure you have Python and all the dependencies installed (Mentioned in <a href="#requisites">Requisites</a>).</li>
<li>Download the files and extract.</li>
<li><b>sudo ./install</b> will install the plugin.</li>
<li>Change the <i>Build System</i> (<i>Tools -> Build System</i>) to <b>TOJHelper</b>.</li>
<li>GoTo <i>TOJHelper -> JudgeId & LanguageId</i> and set your JudgeId and LanguageId.</li>
<li>If you are working behind proxy, goto <i>TOJHelper -> Proxy</i> and set the proxy.</li>
</ol>



<a name="usage"><h3>Usage</h3></a>
<ul>
<li>After the installation, you should see a new menu in the menu bar, <b>Buggy</b>.</li>
<li>Click on the <b>Buggy</b> menu and you&#39;ll be able to see all the options there.
	<ul>
	<li>If you are not able to see all the options, <b>"Tools -> Build System"</b> and select <b>CF</b>.</li>
	</ul>
</li>
<li>Make sure the <b>name of the file is same as the question number</b>. Example : 1234.cpp</li>
<li>Make sure Sublime Side-Bar is visible (<b>View -> Side Bar -> Show Side Bar</b>).</li>
<li>To start parsing the test-cases, <b>(TOJHelper -> Start)</b>.</li>
<li>For parsing the test-cases, provide the question number.</li>
<li>Compile the code before running it on test-cases (<b>Ctrl+B</b> or <b>TOJHelper -> Compile</b>)</li>
<li>To Run the code (<b>TOJHelper -> Run -> Batch Test / Custom Test</b>)</li>
<li>If you want you can change the key-bindings too.</li>
<li>If you are working behind proxy, goto <i>TOJHelper -> Proxy</i> and set the proxy.</li>
</ul>


<a name="techused"><h3>Technology Used</h3></a>
<ul>
<li>Python modules <b>mechanize</b> and <b>BeautifulSoup</b>.</li>
</ul>

<a name="testing"><h3>Testing</h3></a>
The program has been tested on Ubuntu14.04, 64-bit

<a name="contributors"><h3>Contributors</h3></a>
<ol>
	<li><a href="https://github.com/henadaus">Hena Firdaus</a></li>
	<li><a href="https://github.com/pakhandi">Asim Krishna Prasad</a></li>
</ol>

For Hugs and Bugs drop a mail at <b>asimkprasad@gmail.com</b>

