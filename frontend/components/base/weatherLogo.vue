<template>
    <NuxtLink class="logo" to="/weatherAI">
        <img src="/Header/small_logo.png" alt="" class="logo__photo">
        <div class="logo__text">Weather AI</div>
    </NuxtLink>
</template>

<style>
    .logo{
		display: flex;
		align-items: center;
		cursor: pointer;
		text-decoration: none;
		color: black;
	}
    .logo__photo{
		display: block;
		width: 38px;
		height: 38px;
		border-radius: 9px;
	}
	.logo__text{
		margin-left: 14px;
		text-transform: uppercase;
	}
</style>