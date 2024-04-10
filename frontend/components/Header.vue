<template>
	<header class="header">
		<BaseWeatherLogo/>
		<div class="location">
			<div class="location__name">Location: </div>
			<div class="location__place">OLD TOWN, KOSICE, SK</div>
		</div>
	</header>
</template>

<script>
import WeatherLogo from './base/weatherLogo.vue';

</script>

<style scoped>
	.header{
		display: flex;
		margin: 70px auto 0 auto;
		width: 100%;
		justify-content: space-between;
		font-weight: 500;
	}
	.location{
		display: flex;
		align-items: center;
		cursor: pointer;
	}
	.location__place {
		margin-left: 45px;
		cursor: pointer;
	}
</style>