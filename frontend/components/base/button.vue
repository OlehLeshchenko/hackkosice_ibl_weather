<template>
	<NuxtLink class="base-button" to="/weatherAI">
		<slot>Open the forecast</slot>
	</NuxtLink>
</template>

<style scoped>  
    .base-button{
        display: block;
        cursor: pointer;
        text-transform: uppercase;
        padding: 18px 30px;
        color: #FFFFFF;
        font-size: 16px;
        font-weight: bold;
        background-color: #2B6769;
        border-radius: 10px;
        border: none;
        max-width: 276px;
        text-align: center;
        text-decoration: none;
    }
    .base-button:hover{
        color: #2B6769;
        background-color: transparent;
        border: 2px solid #2B6769;
        padding: 16px 28px;
    }
</style>