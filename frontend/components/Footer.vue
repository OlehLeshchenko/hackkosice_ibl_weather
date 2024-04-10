<template>
    <footer class="footer">
        <div class="container">
            <div class="footer__links">
                <BaseWeatherLogo/>
                <NuxtLink to="/weatherAI" class="footer_link">open the forecast</NuxtLink>
            </div>
            <div class="rights">2024 © All rights reserved</div>
        </div>
    </footer>
</template>

<style scoped>
    .logo{
        color: #FFF;
    }
	.footer{
        height: 260px;
        width: 100%;
        background: var(--dark-theme-color, #2B6769);
    }
    .footer__links{
        margin-top: 70px;
        color: #FFF;
        display: flex;
        justify-content: space-between;
    }
    .rights{
        margin-top: 95px;
        color: #FFF;
        text-align: center;
        font-size: 17px;
        font-weight: 500;
        line-height: 136.7%; /* 23.239px */
    }
    .footer_link{
        cursor: pointer;
        text-decoration: none;
        text-transform: uppercase;
        color: #FFF;
        font-size: 19px;
        font-weight: 500;
        line-height: 136.7%;
    }
</style>