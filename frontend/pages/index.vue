<template>
	<div class="main">
		<div class="first-screen-section">
			<div class="container">
				<Header/>
				<div class="info-section">
					<h1 class="info-section__title">Weather Data and AI</h1>
					<div class="info-section__content">Welcome to WeatherAI: Your guide for weather occasions. Let's leverage cutting-edge technology to transform weather insights into actionable decisions for a brighter tomorrow!</div>
					<BaseButton/>
				</div>
				<svg class="big-logo" xmlns="http://www.w3.org/2000/svg" width="954" height="525" viewBox="0 0 954 525" fill="none">
					<path d="M318.425 50.0201C513.129 1.23363 839.565 85.0754 947.067 10.0421C940.833 27.7636 939.92 42.9309 923.519 76.9898C923.519 76.9898 910.611 138.829 851.57 237.546C792.53 336.263 729.054 384.741 618.221 385.585C507.388 386.429 450.115 379.56 313.958 395.836C192.961 410.299 68.2728 453.242 4.57538 514.918C6.80775 492.271 11.7402 455.627 15.0812 434.533C15.6382 430.14 16.421 425.575 17.4611 420.864C49.6236 251.382 179.366 84.8639 318.425 50.0201Z" fill="url(#paint0_linear_2_21)"/>
					<path d="M15.0812 434.533C11.7402 455.627 6.80774 492.271 4.57538 514.918C68.2728 453.242 192.961 410.299 313.958 395.836C450.115 379.56 507.388 386.429 618.221 385.585C729.054 384.741 792.53 336.263 851.57 237.546C910.611 138.829 923.519 76.9898 923.519 76.9898M15.0812 434.533C42.6568 260.427 175.629 85.8003 318.426 50.0201C513.129 1.23363 839.565 85.0754 947.067 10.0421C940.833 27.7636 939.92 42.9309 923.519 76.9898M15.0812 434.533C23.4063 368.868 82.1808 264.952 296.684 206.109C389.663 180.603 505.203 184.058 659.134 187.561C760.02 189.856 866.115 196.196 923.519 76.9898" stroke="url(#paint1_linear_2_21)" stroke-width="7"/>
					<defs>
						<linearGradient id="paint0_linear_2_21" x1="990.959" y1="25.4805" x2="-56.2095" y2="492.766" gradientUnits="userSpaceOnUse">
						<stop stop-color="#9DB9FF"/>
						<stop offset="1" stop-color="#95FFAC"/>
						</linearGradient>
						<linearGradient id="paint1_linear_2_21" x1="236.145" y1="563.51" x2="755.863" y2="-37.4933" gradientUnits="userSpaceOnUse">
						<stop stop-color="white"/>
						<stop offset="1" stop-color="white" stop-opacity="0"/>
						</linearGradient>
					</defs>
				</svg>
			</div>
		</div>

		<div class="about-weather-section section">
			<div class="container">
				<h2 class="section__title">About Weather AI</h2>
				<div class="about-weather__inner">
					<div class="offers">
						<div class="offer">
							<img src="/offers/offer_01.png" alt="" class="offer__logo">
							<div class="offer__content">
								<div class="offer__title">Our Mission</div>
								<div class="offer__text">At WeatherAI, we're dedicated to merging weather data with AI for informed decision-making.</div>
							</div>
						</div>
						<div class="offer">
							<img src="/offers/offer_02.png" alt="" class="offer__logo">
							<div class="offer__content">
								<div class="offer__title">AI Recommendations</div>
								<div class="offer__text">Recommendations powered by AI algorithms, revolutionizing how you respond to weather challenges effectively.</div>
							</div>
						</div>
						<div class="offer">
							<img src="/offers/offer_03.png" alt="" class="offer__logo">
							<div class="offer__content">
								<div class="offer__title">Stay safe with us</div>
								<div class="offer__text">WeatherAI’s accurate forecasts and AI-powered alerts for proactive risk management and preparedness.</div>
							</div>
						</div>
						<div class="offer">
							<img src="/offers/offer_04.png" alt="" class="offer__logo">
							<div class="offer__content">
								<div class="offer__title">Reports & Statistics</div>
								<div class="offer__text">Access reports and statistics, providing deep insights into weather patterns and trends for informed decision-making.</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<hr class="decoration-line"/>
		<div class="team-section section">
			<div class="container">
				<div class="section__title">Our team</div>
				<div class="team_content">
					<svg class="arrow-left" xmlns="http://www.w3.org/2000/svg" width="33" height="50" viewBox="0 0 33 50" fill="none">
  						<path d="M27.5 2L4.5 25L27.5 48" stroke="#2B6769" stroke-width="3"/>
					</svg>

					<div class="team__member-cards">
						<div class="member-card">
							<img src="/members/member_01.png" alt="" class="member-photo">
							<div class="member-pos">Team lead/Designer</div>
							<div class="member-name">Diana Osyka</div>
						</div>
						<div class="member-card">
							<img src="/members/member_02.png" alt="" class="member-photo">
							<div class="member-pos">Front-end developer</div>
							<div class="member-name">Oleh Leshchenko</div>
						</div>
						<div class="member-card">
							<img src="/members/member_03.png" alt="" class="member-photo">
							<div class="member-pos">Back-end developer</div>
							<div class="member-name">Vlad Makoda</div>
						</div>
						<div class="member-card">
							<img src="/members/member_04.png" alt="" class="member-photo">
							<div class="member-pos">Back-end developer</div>
							<div class="member-name">Daniil Kucherenko</div>
						</div>
					</div>
					
					<svg class="arrow-right" xmlns="http://www.w3.org/2000/svg" width="33" height="50" viewBox="0 0 33 50" fill="none">
  						<path d="M5.5 2L28.5 25L5.5 48" stroke="#2B6769" stroke-width="3"/>
					</svg>
				</div>
			</div>
		</div>
		<Footer/>
	</div>
</template>

<style>
@import 'normalize.css/normalize.css';
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: 'Montserrat', sans-serif;
}
.main{
	display: flex;
  	flex-direction: column;
	min-height: 100dvh;
}
.first-screen-section{
	position: relative;
	width: 100%;
	height: 757px;
	background: linear-gradient(180deg, #9AB7FF 0%, #95FAB3 100%);
}
.container{
	display: flex;
	flex-direction: column;
	width: 1340px;
	margin: auto;
	flex: 1;
}
.info-section{
	margin-top: 80px;
	display: flex;
	flex-direction: column;
	width: 490px;
}
.info-section__title{
	margin: 0;
	font-size: 60px;
	font-weight: 900;
	line-height: 136.7%; /* 82.02px */
}
.info-section__content{
	margin: 50px 0;
	font-size: 17px;
	font-weight: 500;
	line-height: 136.7%; /* 82.02px */
}
.big-logo{
	position: absolute;
	top: 150px;
	right: 150px;
}
.section{
	margin: 140px 0;
}
.about-weather__inner{
	margin-top: 70px;
}
.offers{
	margin: auto;
	width: 650px;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: flex-start;
	gap: 44px;
}
.offer{
	display: flex;
}
.offer__logo{
	display: block;
	width: 65px;
	height: 65px;
}
.offer__content{
	margin-left: 40px;
}
.offer__title{
	font-size: 22px;
	font-weight: 700;
	line-height: 136.7%; /* 30.074px */
}
.offer__text{
	font-size: 17px;
	font-weight: 500;
	line-height: 136.7%; /* 23.239px */
}
.section__title{
	text-align: center;	
	font-size: 35px;
	font-weight: 700;
	line-height: 136.7%; /* 47.845px */
}
.decoration-line{
	border: 1px solid #2B6769;
}
.team_content{
	margin-top: 70px;
	display: flex;
	align-items: center;
}
.team__member-cards{
	flex: 1;
	display: flex;
	justify-content: space-between;
	padding: 0 58px;
}
.member-pos{
	margin-top: 20px;
	color: var(--dark-theme-color, #2B6769);
	text-align: center;
	font-size: 17px;
	font-weight: 500;
	line-height: 136.7%; /* 23.239px */
}
.member-name{
	margin-top: 4px;
	color: #000;
	text-align: center;
	font-size: 17px;
	font-weight: 500;
	line-height: 136.7%; /* 23.239px */
}
.arrow-left, .arrow-right{
	cursor: pointer;
}
</style>