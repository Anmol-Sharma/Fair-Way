<!doctype html>
<html class="">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
		<meta name="description" content="We’re on a journey to advance and democratize artificial intelligence through open source and open science." />
		<meta property="fb:app_id" content="1321688464574422" />
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:site" content="@huggingface" />
		<meta name="twitter:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/datasets/mozilla-foundation/common_voice_13_0.png" />
		<meta property="og:title" content="README.md · mozilla-foundation/common_voice_13_0 at main" />
		<meta property="og:type" content="website" />
		<meta property="og:url" content="https://huggingface.co/datasets/mozilla-foundation/common_voice_13_0/blob/main/README.md" />
		<meta property="og:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/datasets/mozilla-foundation/common_voice_13_0.png" />

		<link rel="stylesheet" href="/front/build/kube-a9fae47/style.css" />

		<link rel="preconnect" href="https://fonts.gstatic.com" />
		<link
			href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&display=swap"
			rel="stylesheet"
		/>
		<link
			href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap"
			rel="stylesheet"
		/>

		<link
			rel="preload"
			href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css"
			as="style"
			onload="this.onload=null;this.rel='stylesheet'"
		/>
		<noscript>
			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css" />
		</noscript>

		<script>const guestTheme = document.cookie.match(/theme=(\w+)/)?.[1]; document.documentElement.classList.toggle('dark', guestTheme === 'dark' || ( (!guestTheme || guestTheme === 'system') && window.matchMedia('(prefers-color-scheme: dark)').matches));</script>
<link rel="canonical" href="https://huggingface.co/datasets/mozilla-foundation/common_voice_13_0/blob/main/README.md">  

		<title>README.md · mozilla-foundation/common_voice_13_0 at main</title>

		<script
			defer
			data-domain="huggingface.co"
			event-loggedIn="false"
			src="/js/script.pageview-props.js"
		></script>
		<script>
			window.plausible =
				window.plausible ||
				function () {
					(window.plausible.q = window.plausible.q || []).push(arguments);
				};
		</script>
		<script>
			window.hubConfig = {"features":{"signupDisabled":false},"sshGitUrl":"git@hf.co","moonHttpUrl":"https:\/\/huggingface.co","captchaApiKey":"bd5f2066-93dc-4bdd-a64b-a24646ca3859","captchaDisabledOnSignup":true,"datasetViewerPublicUrl":"https:\/\/datasets-server.huggingface.co","stripePublicKey":"pk_live_x2tdjFXBCvXo2FFmMybezpeM00J6gPCAAc","environment":"production","userAgent":"HuggingFace (production)","spacesIframeDomain":"hf.space","spacesApiUrl":"https:\/\/api.hf.space","docSearchKey":"ece5e02e57300e17d152c08056145326e90c4bff3dd07d7d1ae40cf1c8d39cb6","logoDev":{"apiUrl":"https:\/\/img.logo.dev\/","apiKey":"pk_UHS2HZOeRnaSOdDp7jbd5w"}};
		</script>
		<script type="text/javascript" src="https://de5282c3ca0c.edge.sdk.awswaf.com/de5282c3ca0c/526cf06acb0d/challenge.js" defer></script>
	</head>
	<body class="flex flex-col min-h-dvh bg-white dark:bg-gray-950 text-black ViewerBlobPage">
		<div class="flex min-h-dvh flex-col"><div class="SVELTE_HYDRATER contents" data-target="SystemThemeMonitor" data-props="{&quot;isLoggedIn&quot;:false}"></div>

	<div class="SVELTE_HYDRATER contents" data-target="MainHeader" data-props="{&quot;classNames&quot;:&quot;&quot;,&quot;isWide&quot;:false,&quot;isZh&quot;:false,&quot;isPro&quot;:false}"><header class="border-b border-gray-100 "><div class="w-full px-4 container flex h-16 items-center"><div class="flex flex-1 items-center"><a class="mr-5 flex flex-none items-center lg:mr-6" href="/"><img alt="Hugging Face's logo" class="w-7 md:mr-2" src="/front/assets/huggingface_logo-noborder.svg">
				<span class="hidden whitespace-nowrap text-lg font-bold md:block">Hugging Face</span></a>
			<div class="relative flex-1 lg:max-w-sm mr-2 sm:mr-4 md:mr-3 xl:mr-6"><input autocomplete="off" class="w-full dark:bg-gray-950 pl-8 form-input-alt h-9 pr-3 focus:shadow-xl " name="" placeholder="Search models, datasets, users..."   spellcheck="false" type="text" value="">
	<svg class="absolute left-2.5 text-gray-400 top-1/2 transform -translate-y-1/2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M30 28.59L22.45 21A11 11 0 1 0 21 22.45L28.59 30zM5 14a9 9 0 1 1 9 9a9 9 0 0 1-9-9z" fill="currentColor"></path></svg>
	</div>
			<div class="flex flex-none items-center justify-center p-0.5 place-self-stretch lg:hidden"><button class="relative z-40 flex h-6 w-8 items-center justify-center" type="button"><svg width="1em" height="1em" viewBox="0 0 10 10" class="text-xl" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.65039 2.9999C1.65039 2.8066 1.80709 2.6499 2.00039 2.6499H8.00039C8.19369 2.6499 8.35039 2.8066 8.35039 2.9999C8.35039 3.1932 8.19369 3.3499 8.00039 3.3499H2.00039C1.80709 3.3499 1.65039 3.1932 1.65039 2.9999ZM1.65039 4.9999C1.65039 4.8066 1.80709 4.6499 2.00039 4.6499H8.00039C8.19369 4.6499 8.35039 4.8066 8.35039 4.9999C8.35039 5.1932 8.19369 5.3499 8.00039 5.3499H2.00039C1.80709 5.3499 1.65039 5.1932 1.65039 4.9999ZM2.00039 6.6499C1.80709 6.6499 1.65039 6.8066 1.65039 6.9999C1.65039 7.1932 1.80709 7.3499 2.00039 7.3499H8.00039C8.19369 7.3499 8.35039 7.1932 8.35039 6.9999C8.35039 6.8066 8.19369 6.6499 8.00039 6.6499H2.00039Z"></path></svg>
		</button>

	</div></div>
		<nav aria-label="Main" class="ml-auto hidden lg:block"><ul class="flex items-center space-x-1.5 2xl:space-x-2"><li class="hover:text-indigo-700"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/models"><svg class="mr-1.5 text-gray-400 group-hover:text-indigo-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
					Models</a>
			</li><li class="hover:text-red-700"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/datasets"><svg class="mr-1.5 text-gray-400 group-hover:text-red-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
					Datasets</a>
			</li><li class="hover:text-blue-700"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/spaces"><svg class="mr-1.5 text-gray-400 group-hover:text-blue-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 25 25"><path opacity=".5" d="M6.016 14.674v4.31h4.31v-4.31h-4.31ZM14.674 14.674v4.31h4.31v-4.31h-4.31ZM6.016 6.016v4.31h4.31v-4.31h-4.31Z" fill="currentColor"></path><path opacity=".75" fill-rule="evenodd" clip-rule="evenodd" d="M3 4.914C3 3.857 3.857 3 4.914 3h6.514c.884 0 1.628.6 1.848 1.414a5.171 5.171 0 0 1 7.31 7.31c.815.22 1.414.964 1.414 1.848v6.514A1.914 1.914 0 0 1 20.086 22H4.914A1.914 1.914 0 0 1 3 20.086V4.914Zm3.016 1.102v4.31h4.31v-4.31h-4.31Zm0 12.968v-4.31h4.31v4.31h-4.31Zm8.658 0v-4.31h4.31v4.31h-4.31Zm0-10.813a2.155 2.155 0 1 1 4.31 0 2.155 2.155 0 0 1-4.31 0Z" fill="currentColor"></path><path opacity=".25" d="M16.829 6.016a2.155 2.155 0 1 0 0 4.31 2.155 2.155 0 0 0 0-4.31Z" fill="currentColor"></path></svg>
					Spaces</a>
			</li><li class="hover:text-yellow-700 max-xl:hidden"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/posts"><svg class="mr-1.5 text-gray-400 group-hover:text-yellow-500 text-yellow-500!" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 12 12" preserveAspectRatio="xMidYMid meet"><path fill="currentColor" fill-rule="evenodd" d="M3.73 2.4A4.25 4.25 0 1 1 6 10.26H2.17l-.13-.02a.43.43 0 0 1-.3-.43l.01-.06a.43.43 0 0 1 .12-.22l.84-.84A4.26 4.26 0 0 1 3.73 2.4Z" clip-rule="evenodd"></path></svg>
					Posts</a>
			</li><li class="hover:text-yellow-700"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/docs"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1.5 text-gray-400 group-hover:text-yellow-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><path d="m2.28 3.7-.3.16a.67.67 0 0 0-.34.58v8.73l.01.04.02.07.01.04.03.06.02.04.02.03.04.06.05.05.04.04.06.04.06.04.08.04.08.02h.05l.07.02h.11l.04-.01.07-.02.03-.01.07-.03.22-.12a5.33 5.33 0 0 1 5.15.1.67.67 0 0 0 .66 0 5.33 5.33 0 0 1 5.33 0 .67.67 0 0 0 1-.58V4.36a.67.67 0 0 0-.34-.5l-.3-.17v7.78a.63.63 0 0 1-.87.59 4.9 4.9 0 0 0-4.35.35l-.65.39a.29.29 0 0 1-.15.04.29.29 0 0 1-.16-.04l-.65-.4a4.9 4.9 0 0 0-4.34-.34.63.63 0 0 1-.87-.59V3.7Z" fill="currentColor" class="dark:opacity-40"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M8 3.1a5.99 5.99 0 0 0-5.3-.43.66.66 0 0 0-.42.62v8.18c0 .45.46.76.87.59a4.9 4.9 0 0 1 4.34.35l.65.39c.05.03.1.04.16.04.05 0 .1-.01.15-.04l.65-.4a4.9 4.9 0 0 1 4.35-.34.63.63 0 0 0 .86-.59V3.3a.67.67 0 0 0-.41-.62 5.99 5.99 0 0 0-5.3.43l-.3.17L8 3.1Zm.73 1.87a.43.43 0 1 0-.86 0v5.48a.43.43 0 0 0 .86 0V4.97Z" fill="currentColor" class="opacity-40 dark:opacity-100"></path><path d="M8.73 4.97a.43.43 0 1 0-.86 0v5.48a.43.43 0 1 0 .86 0V4.96Z" fill="currentColor" class="dark:opacity-40"></path></svg>
					Docs</a>
			</li><li class="hover:text-black dark:hover:text-white"><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/enterprise"><svg class="mr-1.5 text-gray-400 group-hover:text-black dark:group-hover:text-white" xmlns="http://www.w3.org/2000/svg" fill="none" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 33 27"><path fill="currentColor" fill-rule="evenodd" d="M13.5.7a8.7 8.7 0 0 0-7.7 5.7L1 20.6c-1 3.1.9 5.7 4.1 5.7h15c3.3 0 6.8-2.6 7.8-5.7l4.6-14.2c1-3.1-.8-5.7-4-5.7h-15Zm1.1 5.7L9.8 20.3h9.8l1-3.1h-5.8l.8-2.5h4.8l1.1-3h-4.8l.8-2.3H23l1-3h-9.5Z" clip-rule="evenodd"></path></svg>
					Enterprise</a>
			</li>

		<li><a class="group flex items-center px-2 py-0.5 dark:text-gray-300 dark:hover:text-gray-100" href="/pricing">Pricing
			</a></li>

		<li><div class="relative group">
	<button class="px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-600 flex items-center " type="button">
		<svg class=" text-gray-500 w-5 group-hover:text-gray-400 dark:text-gray-300 dark:group-hover:text-gray-100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 18" preserveAspectRatio="xMidYMid meet"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 3.30221C14.4504 2.836 14.8284 2.45807 15.2946 2.45807H28.4933C28.9595 2.45807 29.3374 2.836 29.3374 3.30221C29.3374 3.76842 28.9595 4.14635 28.4933 4.14635H15.2946C14.8284 4.14635 14.4504 3.76842 14.4504 3.30221Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 9.00002C14.4504 8.53382 14.8284 8.15588 15.2946 8.15588H28.4933C28.9595 8.15588 29.3374 8.53382 29.3374 9.00002C29.3374 9.46623 28.9595 9.84417 28.4933 9.84417H15.2946C14.8284 9.84417 14.4504 9.46623 14.4504 9.00002Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 14.6978C14.4504 14.2316 14.8284 13.8537 15.2946 13.8537H28.4933C28.9595 13.8537 29.3374 14.2316 29.3374 14.6978C29.3374 15.164 28.9595 15.542 28.4933 15.542H15.2946C14.8284 15.542 14.4504 15.164 14.4504 14.6978Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M1.94549 6.87377C2.27514 6.54411 2.80962 6.54411 3.13928 6.87377L6.23458 9.96907L9.32988 6.87377C9.65954 6.54411 10.194 6.54411 10.5237 6.87377C10.8533 7.20343 10.8533 7.73791 10.5237 8.06756L6.23458 12.3567L1.94549 8.06756C1.61583 7.73791 1.61583 7.20343 1.94549 6.87377Z" fill="currentColor"></path></svg>
			
		</button>
	
	
	</div></li>
		<li><hr class="h-5 w-0.5 border-none bg-gray-100 dark:bg-gray-800"></li>
		<li><a class="block cursor-pointer whitespace-nowrap px-2 py-0.5 hover:text-gray-500 dark:text-gray-300 dark:hover:text-gray-100" href="/login">Log In
				</a></li>
			<li><a class="whitespace-nowrap rounded-full border border-transparent bg-gray-900 px-3 py-1 leading-none text-white hover:border-black hover:bg-white hover:text-black" href="/join">Sign Up
					</a></li></ul></nav></div></header></div>
	
	
	
	<div class="SVELTE_HYDRATER contents" data-target="SSOBanner" data-props="{}"></div>
	
	

	<main class="flex flex-1 flex-col"><div class="SVELTE_HYDRATER contents" data-target="DatasetHeader" data-props="{&quot;activeTab&quot;:&quot;files&quot;,&quot;author&quot;:{&quot;avatarUrl&quot;:&quot;https://cdn-avatars.huggingface.co/v1/production/uploads/1638460472471-602e6dee60e3dd96631c906e.jpeg&quot;,&quot;fullname&quot;:&quot;Mozilla Foundation&quot;,&quot;name&quot;:&quot;mozilla-foundation&quot;,&quot;type&quot;:&quot;org&quot;,&quot;isHf&quot;:false,&quot;isHfAdmin&quot;:false,&quot;isMod&quot;:false,&quot;isEnterprise&quot;:false,&quot;followerCount&quot;:191},&quot;canReadRepoSettings&quot;:false,&quot;dataset&quot;:{&quot;author&quot;:&quot;mozilla-foundation&quot;,&quot;cardData&quot;:{&quot;pretty_name&quot;:&quot;Common Voice Corpus 13.0&quot;,&quot;annotations_creators&quot;:[&quot;crowdsourced&quot;],&quot;language_creators&quot;:[&quot;crowdsourced&quot;],&quot;language_bcp47&quot;:[&quot;ab&quot;,&quot;ar&quot;,&quot;as&quot;,&quot;ast&quot;,&quot;az&quot;,&quot;ba&quot;,&quot;bas&quot;,&quot;be&quot;,&quot;bg&quot;,&quot;bn&quot;,&quot;br&quot;,&quot;ca&quot;,&quot;ckb&quot;,&quot;cnh&quot;,&quot;cs&quot;,&quot;cv&quot;,&quot;cy&quot;,&quot;da&quot;,&quot;de&quot;,&quot;dv&quot;,&quot;dyu&quot;,&quot;el&quot;,&quot;en&quot;,&quot;eo&quot;,&quot;es&quot;,&quot;et&quot;,&quot;eu&quot;,&quot;fa&quot;,&quot;fi&quot;,&quot;fr&quot;,&quot;fy-NL&quot;,&quot;ga-IE&quot;,&quot;gl&quot;,&quot;gn&quot;,&quot;ha&quot;,&quot;hi&quot;,&quot;hsb&quot;,&quot;hu&quot;,&quot;hy-AM&quot;,&quot;ia&quot;,&quot;id&quot;,&quot;ig&quot;,&quot;is&quot;,&quot;it&quot;,&quot;ja&quot;,&quot;ka&quot;,&quot;kab&quot;,&quot;kk&quot;,&quot;kmr&quot;,&quot;ko&quot;,&quot;ky&quot;,&quot;lg&quot;,&quot;lo&quot;,&quot;lt&quot;,&quot;lv&quot;,&quot;mdf&quot;,&quot;mhr&quot;,&quot;mk&quot;,&quot;ml&quot;,&quot;mn&quot;,&quot;mr&quot;,&quot;mrj&quot;,&quot;mt&quot;,&quot;myv&quot;,&quot;nan-tw&quot;,&quot;ne-NP&quot;,&quot;nl&quot;,&quot;nn-NO&quot;,&quot;oc&quot;,&quot;or&quot;,&quot;pa-IN&quot;,&quot;pl&quot;,&quot;pt&quot;,&quot;quy&quot;,&quot;rm-sursilv&quot;,&quot;rm-vallader&quot;,&quot;ro&quot;,&quot;ru&quot;,&quot;rw&quot;,&quot;sah&quot;,&quot;sat&quot;,&quot;sc&quot;,&quot;sk&quot;,&quot;skr&quot;,&quot;sl&quot;,&quot;sr&quot;,&quot;sv-SE&quot;,&quot;sw&quot;,&quot;ta&quot;,&quot;th&quot;,&quot;ti&quot;,&quot;tig&quot;,&quot;tk&quot;,&quot;tok&quot;,&quot;tr&quot;,&quot;tt&quot;,&quot;tw&quot;,&quot;ug&quot;,&quot;uk&quot;,&quot;ur&quot;,&quot;uz&quot;,&quot;vi&quot;,&quot;vot&quot;,&quot;yo&quot;,&quot;yue&quot;,&quot;zh-CN&quot;,&quot;zh-HK&quot;,&quot;zh-TW&quot;],&quot;license&quot;:[&quot;cc0-1.0&quot;],&quot;multilinguality&quot;:[&quot;multilingual&quot;],&quot;source_datasets&quot;:[&quot;extended|common_voice&quot;],&quot;task_categories&quot;:[&quot;automatic-speech-recognition&quot;],&quot;paperswithcode_id&quot;:&quot;common-voice&quot;,&quot;extra_gated_prompt&quot;:&quot;By clicking on “Access repository” below, you also agree to not attempt to determine the identity of speakers in the Common Voice dataset.&quot;},&quot;cardError&quot;:{&quot;errors&quot;:[{&quot;message&quot;:&quot;\&quot;size_categories\&quot; must be a string&quot;,&quot;path&quot;:[&quot;size_categories&quot;]}],&quot;warnings&quot;:[]},&quot;cardExists&quot;:true,&quot;createdAt&quot;:&quot;2023-03-29T07:43:24.000Z&quot;,&quot;citation&quot;:&quot;@inproceedings{commonvoice:2020,\n  author = {Ardila, R. and Branson, M. and Davis, K. and Henretty, M. and Kohler, M. and Meyer, J. and Morais, R. and Saunders, L. and Tyers, F. M. and Weber, G.},\n  title = {Common Voice: A Massively-Multilingual Speech Corpus},\n  booktitle = {Proceedings of the 12th Conference on Language Resources and Evaluation (LREC 2020)},\n  pages = {4211--4215},\n  year = 2020\n}&quot;,&quot;description&quot;:&quot;\n\t\n\t\t\n\t\n\t\n\t\tDataset Card for Common Voice Corpus 13.0\n\t\n\n\n\t\n\t\t\n\t\n\t\n\t\tDataset Summary\n\t\n\nThe Common Voice dataset consists of a unique MP3 and corresponding text file. \nMany of the 27141 recorded hours in the dataset also include demographic metadata like age, sex, and accent \nthat can help improve the accuracy of speech recognition engines.\nThe dataset currently consists of 17689 validated hours in 108 languages, but more voices and languages are always added. \nTake a look at the Languages… See the full description on the dataset page: https://huggingface.co/datasets/mozilla-foundation/common_voice_13_0.&quot;,&quot;downloads&quot;:7782,&quot;downloadsAllTime&quot;:619206,&quot;id&quot;:&quot;mozilla-foundation/common_voice_13_0&quot;,&quot;isLikedByUser&quot;:false,&quot;lastModified&quot;:&quot;2023-06-26T15:23:12.000Z&quot;,&quot;likes&quot;:177,&quot;paperswithcode_id&quot;:&quot;common-voice&quot;,&quot;datasetsServerInfo&quot;:{&quot;viewer&quot;:&quot;viewer-partial&quot;,&quot;numRows&quot;:7176573,&quot;libraries&quot;:[&quot;datasets&quot;,&quot;mlcroissant&quot;],&quot;formats&quot;:[],&quot;modalities&quot;:[&quot;audio&quot;,&quot;text&quot;]},&quot;discussionsDisabled&quot;:false,&quot;repoType&quot;:&quot;dataset&quot;,&quot;private&quot;:false,&quot;gated&quot;:&quot;auto&quot;,&quot;tags&quot;:[&quot;task_categories:automatic-speech-recognition&quot;,&quot;annotations_creators:crowdsourced&quot;,&quot;language_creators:crowdsourced&quot;,&quot;multilinguality:multilingual&quot;,&quot;source_datasets:extended|common_voice&quot;,&quot;license:cc0-1.0&quot;,&quot;size_categories:1M<n<10M&quot;,&quot;modality:audio&quot;,&quot;modality:text&quot;,&quot;library:datasets&quot;,&quot;library:mlcroissant&quot;,&quot;arxiv:1912.06670&quot;,&quot;region:us&quot;],&quot;tag_objs&quot;:[{&quot;id&quot;:&quot;task_categories:automatic-speech-recognition&quot;,&quot;label&quot;:&quot;automatic-speech-recognition&quot;,&quot;type&quot;:&quot;task_categories&quot;,&quot;subType&quot;:&quot;audio&quot;},{&quot;id&quot;:&quot;annotations_creators:crowdsourced&quot;,&quot;label&quot;:&quot;crowdsourced&quot;,&quot;type&quot;:&quot;annotations_creators&quot;},{&quot;id&quot;:&quot;language_creators:crowdsourced&quot;,&quot;label&quot;:&quot;crowdsourced&quot;,&quot;type&quot;:&quot;language_creators&quot;},{&quot;id&quot;:&quot;multilinguality:multilingual&quot;,&quot;label&quot;:&quot;multilingual&quot;,&quot;type&quot;:&quot;multilinguality&quot;},{&quot;id&quot;:&quot;source_datasets:extended|common_voice&quot;,&quot;label&quot;:&quot;extended|common_voice&quot;,&quot;type&quot;:&quot;source_datasets&quot;},{&quot;id&quot;:&quot;license:cc0-1.0&quot;,&quot;label&quot;:&quot;cc0-1.0&quot;,&quot;type&quot;:&quot;license&quot;},{&quot;id&quot;:&quot;size_categories:1M<n<10M&quot;,&quot;label&quot;:&quot;1M - 10M&quot;,&quot;type&quot;:&quot;size_categories&quot;},{&quot;id&quot;:&quot;modality:audio&quot;,&quot;label&quot;:&quot;Audio&quot;,&quot;type&quot;:&quot;modality&quot;},{&quot;id&quot;:&quot;modality:text&quot;,&quot;label&quot;:&quot;Text&quot;,&quot;type&quot;:&quot;modality&quot;},{&quot;id&quot;:&quot;library:datasets&quot;,&quot;label&quot;:&quot;Datasets&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;library:mlcroissant&quot;,&quot;label&quot;:&quot;Croissant&quot;,&quot;type&quot;:&quot;library&quot;},{&quot;id&quot;:&quot;arxiv:1912.06670&quot;,&quot;label&quot;:&quot;arxiv:1912.06670&quot;,&quot;type&quot;:&quot;arxiv&quot;,&quot;extra&quot;:{&quot;paperTitle&quot;:&quot;Common Voice: A Massively-Multilingual Speech Corpus&quot;}},{&quot;type&quot;:&quot;region&quot;,&quot;label&quot;:&quot;🇺🇸 Region: US&quot;,&quot;id&quot;:&quot;region:us&quot;}],&quot;homepage&quot;:&quot;https://commonvoice.mozilla.org/en/datasets&quot;,&quot;hasBlockedOids&quot;:false,&quot;region&quot;:&quot;us&quot;,&quot;xetEnabled&quot;:false},&quot;discussionsStats&quot;:{&quot;closed&quot;:4,&quot;open&quot;:5,&quot;total&quot;:9}}"><header class="bg-linear-to-t border-b border-gray-100 pt-6 sm:pt-9 from-gray-50-to-white via-white dark:via-gray-950"><div class="container relative "><h1 class="flex flex-wrap items-center max-md:leading-tight mb-3 text-lg max-sm:gap-y-1.5 md:text-xl"><a href="/datasets" class="group flex items-center"><svg class="sm:mr-1.5 -mr-1 text-gray-400" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
					<span class="mr-2.5 font-semibold text-gray-400 group-hover:text-gray-500 max-sm:hidden">Datasets:</span></a>
				<hr class="mx-1.5 h-2 translate-y-px rounded-sm border-r dark:border-gray-600 sm:hidden">
			<div class="group flex flex-none items-center"><div class="relative mr-1 flex items-center">

			

<span class="inline-block "><span class="contents"><a href="/mozilla-foundation" class="text-gray-400 hover:text-blue-600"><img alt="" class="w-3.5 h-3.5 rounded-sm  flex-none" src="https://cdn-avatars.huggingface.co/v1/production/uploads/1638460472471-602e6dee60e3dd96631c906e.jpeg" crossorigin="anonymous"></a></span>
	</span></div>
		

<span class="inline-block "><span class="contents"><a href="/mozilla-foundation" class="text-gray-400 hover:text-blue-600">mozilla-foundation</a></span>
	</span>
		<div class="mx-0.5 text-gray-300">/</div></div>

<div class="max-w-full "><a class="break-words font-mono font-semibold hover:text-blue-600 " href="/datasets/mozilla-foundation/common_voice_13_0">common_voice_13_0</a>
	<button class="relative text-sm mr-4 focus:outline-hidden inline-flex cursor-pointer items-center text-sm  mx-0.5   text-gray-600 " title="Copy dataset name to clipboard" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	</button></div>
			<div class="inline-flex items-center overflow-hidden whitespace-nowrap rounded-md border bg-white text-sm leading-none text-gray-500  mr-2"><button class="relative flex items-center overflow-hidden from-red-50 to-transparent dark:from-red-900 px-1.5 py-1 hover:bg-linear-to-t focus:outline-hidden"  title="Like"><svg class="left-1.5 absolute" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.45,6a5.47,5.47,0,0,1,3.91,1.64,5.7,5.7,0,0,1,0,8L16,26.13,5.64,15.64a5.7,5.7,0,0,1,0-8,5.48,5.48,0,0,1,7.82,0L16,10.24l2.53-2.58A5.44,5.44,0,0,1,22.45,6m0-2a7.47,7.47,0,0,0-5.34,2.24L16,7.36,14.89,6.24a7.49,7.49,0,0,0-10.68,0,7.72,7.72,0,0,0,0,10.82L16,29,27.79,17.06a7.72,7.72,0,0,0,0-10.82A7.49,7.49,0,0,0,22.45,4Z"></path></svg>

		
		<span class="ml-4 pl-0.5 ">like</span></button>
	<button class="focus:outline-hidden flex items-center border-l px-1.5 py-1 text-gray-400 hover:bg-gray-50 focus:bg-gray-100 dark:hover:bg-gray-900 dark:focus:bg-gray-800" title="See users who liked this repository">177</button></div>




			<div class="relative flex items-center gap-1.5  "><div class="mr-2 inline-flex h-6 items-center overflow-hidden whitespace-nowrap rounded-md border text-sm text-gray-500"><button class="focus:outline-hidden relative flex h-full max-w-56 items-center gap-1.5 overflow-hidden px-1.5 hover:bg-gray-50 focus:bg-gray-100 dark:hover:bg-gray-900 dark:focus:bg-gray-800" type="button" ><div class="flex h-full flex-1 items-center justify-center ">Follow</div>
		<img alt="" class="rounded-xs size-3 flex-none" src="https://cdn-avatars.huggingface.co/v1/production/uploads/1638460472471-602e6dee60e3dd96631c906e.jpeg">
		<span class="truncate">Mozilla Foundation</span></button>
	<button class="focus:outline-hidden flex h-full items-center border-l pl-1.5 pr-1.5 text-gray-400 hover:bg-gray-50 focus:bg-gray-100 dark:hover:bg-gray-900 dark:focus:bg-gray-800" title="Show Mozilla Foundation's followers" type="button">191</button></div>

		</div>
			
	</h1>
		<div class="mb-3 flex flex-wrap md:mb-4"><div class="mr-1 flex flex-wrap items-center"><span class="mb-1 mr-1 p-1 text-sm leading-tight text-gray-400 md:mb-1.5">Tasks:
	</span>
	<a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/datasets?task_categories=task_categories%3Aautomatic-speech-recognition"><div class="tag tag-white   "><div class="tag-ico -ml-2 tag-ico-yellow"><svg class="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 18 18"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.38893 3.42133C7.9778 3.14662 7.49446 3 7 3C6.33696 3 5.70108 3.26339 5.23223 3.73223C4.76339 4.20107 4.5 4.83696 4.5 5.5C4.5 5.99445 4.64662 6.4778 4.92133 6.88893C5.19603 7.30005 5.58648 7.62048 6.04329 7.8097C6.50011 7.99892 7.00278 8.04843 7.48773 7.95196C7.97268 7.8555 8.41814 7.6174 8.76777 7.26777C9.1174 6.91814 9.3555 6.47268 9.45197 5.98773C9.54843 5.50277 9.49892 5.00011 9.3097 4.54329C9.12048 4.08648 8.80005 3.69603 8.38893 3.42133ZM5.05551 2.58986C5.63108 2.20527 6.30777 2 7 2C7.92826 2 8.8185 2.36875 9.47488 3.02513C10.1313 3.6815 10.5 4.57174 10.5 5.5C10.5 6.19223 10.2947 6.86892 9.91015 7.4445C9.52556 8.02007 8.97894 8.46867 8.33939 8.73358C7.69985 8.99849 6.99612 9.0678 6.31719 8.93275C5.63825 8.7977 5.01461 8.46436 4.52513 7.97487C4.03564 7.48539 3.7023 6.86175 3.56725 6.18282C3.4322 5.50388 3.50152 4.80015 3.76642 4.16061C4.03133 3.52107 4.47993 2.97444 5.05551 2.58986ZM14.85 9.6425L15.7075 10.5C15.8005 10.5927 15.8743 10.7029 15.9245 10.8242C15.9747 10.9456 16.0004 11.0757 16 11.207V16H2V13.5C2.00106 12.5721 2.37015 11.6824 3.0263 11.0263C3.68244 10.3701 4.57207 10.0011 5.5 10H8.5C9.42793 10.0011 10.3176 10.3701 10.9737 11.0263C11.6299 11.6824 11.9989 12.5721 12 13.5V15H15V11.207L14.143 10.35C13.9426 10.4476 13.7229 10.4989 13.5 10.5C13.2033 10.5 12.9133 10.412 12.6666 10.2472C12.42 10.0824 12.2277 9.84811 12.1142 9.57403C12.0006 9.29994 11.9709 8.99834 12.0288 8.70737C12.0867 8.41639 12.2296 8.14912 12.4393 7.93934C12.6491 7.72956 12.9164 7.5867 13.2074 7.52882C13.4983 7.47094 13.7999 7.50065 14.074 7.61418C14.3481 7.72771 14.5824 7.91997 14.7472 8.16665C14.912 8.41332 15 8.70333 15 9C14.9988 9.22271 14.9475 9.44229 14.85 9.6425ZM3.73311 11.7331C3.26444 12.2018 3.00079 12.8372 3 13.5V15H11V13.5C10.9992 12.8372 10.7356 12.2018 10.2669 11.7331C9.79822 11.2644 9.1628 11.0008 8.5 11H5.5C4.8372 11.0008 4.20178 11.2644 3.73311 11.7331Z" fill="currentColor"></path></svg></div>

	

	<span>Automatic Speech Recognition</span>
	

	</div></a>

	</div><div class="mr-1 flex flex-wrap items-center"><span class="mb-1 mr-1 p-1 text-sm leading-tight text-gray-400 md:mb-1.5">Modalities:
	</span>
	<a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/datasets?modality=modality%3Aaudio"><div class="tag tag-white   ">
		<svg class="text-fuchsia-800  dark:text-fuchsia-700" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.619 4.619C2.667 6.573 2.667 9.715 2.667 16s0 9.428 1.952 11.38C6.573 29.333 9.715 29.333 16 29.333s9.428 0 11.38-1.953c1.953-1.95 1.953-5.095 1.953-11.38s0-9.428-1.953-11.381C25.43 2.667 22.285 2.667 16 2.667s-9.428 0-11.381 1.952M17 9.333a1 1 0 1 0-2 0v13.334a1 1 0 0 0 2 0zM10.333 12a1 1 0 0 0-2 0v8a1 1 0 1 0 2 0zm13.334 1.333a1 1 0 0 0-2 0v5.334a1 1 0 1 0 2 0z" fill="currentColor"></path></svg>

	

	<span>Audio</span>
	

	</div></a><a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/datasets?modality=modality%3Atext"><div class="tag tag-white   ">
		<svg class="text-red-700 dark:text-red-600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.619 4.619C2.667 6.573 2.667 9.715 2.667 16s0 9.428 1.952 11.38C6.573 29.333 9.715 29.333 16 29.333s9.428 0 11.38-1.953c1.953-1.95 1.953-5.095 1.953-11.38s0-9.428-1.953-11.381C25.43 2.667 22.285 2.667 16 2.667s-9.428 0-11.381 1.952m8.65 3.714c-.573 0-1.109 0-1.546.066-.495.073-1.003.248-1.41.7-.392.436-.53.956-.59 1.452-.056.464-.056 1.04-.056 1.689V13a1 1 0 1 0 2 0v-.704c0-.724.001-1.176.041-1.505q.015-.15.061-.294a.2.2 0 0 1 .031-.061q0-.003.016-.01a.8.8 0 0 1 .203-.05c.272-.04.654-.043 1.314-.043H15v11.334h-2.333a1 1 0 1 0 0 2H20a1 1 0 0 0 0-2h-3V10.333h1.667c.66 0 1.042.003 1.314.043.123.019.18.04.203.05l.015.009a.2.2 0 0 1 .032.061c.018.05.042.14.061.295.04.329.041.781.041 1.506V13a1 1 0 1 0 2 0v-.76c0-.65 0-1.225-.056-1.69-.06-.495-.198-1.015-.59-1.453-.407-.45-.915-.625-1.41-.698-.437-.067-.973-.067-1.546-.066z" fill="currentColor"></path></svg>

	

	<span>Text</span>
	

	</div></a>

	</div><div class="mr-1 flex flex-wrap items-center"><span class="mb-1 mr-1 p-1 text-sm leading-tight text-gray-400 md:mb-1.5">Size:
	</span>
	<a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/datasets?size_categories=size_categories%3A1M%3Cn%3C10M"><div class="tag tag-white   ">

	

	<span>1M - 10M</span>
	

	</div></a>

	</div><div class="mr-1 flex flex-wrap items-center"><span class="mb-1 mr-1 p-1 text-sm leading-tight text-gray-400 md:mb-1.5">ArXiv:
	</span>
	

	<div class="relative inline-block ">
	<button class="group mr-1 mb-1 md:mr-1.5 md:mb-1.5  rounded-full rounded-br-none " type="button">
		<div class="tag tag-white rounded-full  relative rounded-br-none pr-2.5">
		<svg class="-mr-1 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 12 12" preserveAspectRatio="xMidYMid meet" fill="none"><path fill="currentColor" fill-rule="evenodd" d="M8.007 1.814a1.176 1.176 0 0 0-.732-.266H3.088c-.64 0-1.153.512-1.153 1.152v6.803c0 .64.513 1.152 1.153 1.152h5.54c.632 0 1.144-.511 1.144-1.152V3.816c0-.338-.137-.658-.412-.887L8.007 1.814Zm-1.875 1.81c0 .695.55 1.253 1.244 1.253h.983a.567.567 0 0 1 .553.585v4.041c0 .165-.119.302-.283.302h-5.55c-.156 0-.275-.137-.275-.302V2.7a.284.284 0 0 1 .284-.301h2.468a.574.574 0 0 1 .434.19.567.567 0 0 1 .142.395v.64Z" clip-rule="evenodd"></path><path fill="currentColor" fill-opacity=".2" fill-rule="evenodd" d="M6.132 3.624c0 .695.55 1.253 1.244 1.253h.97a.567.567 0 0 1 .566.585v4.041c0 .165-.119.302-.283.302h-5.55c-.156 0-.275-.137-.275-.302V2.7a.284.284 0 0 1 .284-.301h2.468a.567.567 0 0 1 .576.585v.64Z" clip-rule="evenodd"></path></svg>

	

	<span class="-mr-2 text-gray-400">arxiv:</span>
		<span>1912.06670</span>
	

	<div class="border-br-gray-200 absolute bottom-0.5 right-0.5 h-1 w-1 border-[3px] border-l-transparent border-t-transparent border-b-gray-200 border-r-gray-200 dark:border-b-gray-700 dark:border-r-gray-700"></div></div>
		
		</button>
	
	
	</div>

	</div><div class="mr-1 flex flex-wrap items-center"><span class="mb-1 mr-1 p-1 text-sm leading-tight text-gray-400 md:mb-1.5">Libraries:
	</span>
	<a class="mb-1 mr-1 md:mb-1.5 md:mr-1.5 rounded-lg" href="/datasets?library=library%3Adatasets"><div class="tag tag-white   "><svg class="text-black inline-block text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" width="1em" height="1em" viewBox="0 0 95 88"><path fill="#fff" d="M94.25 70.08a8.28 8.28 0 0 1-.43 6.46 10.57 10.57 0 0 1-3 3.6 25.18 25.18 0 0 1-5.7 3.2 65.74 65.74 0 0 1-7.56 2.65 46.67 46.67 0 0 1-11.42 1.68c-5.42.05-10.09-1.23-13.4-4.5a40.4 40.4 0 0 1-10.14.03c-3.34 3.25-7.99 4.52-13.39 4.47a46.82 46.82 0 0 1-11.43-1.68 66.37 66.37 0 0 1-7.55-2.65c-2.28-.98-4.17-2-5.68-3.2a10.5 10.5 0 0 1-3.02-3.6c-.99-2-1.18-4.3-.42-6.46a8.54 8.54 0 0 1-.33-5.63c.25-.95.66-1.83 1.18-2.61a8.67 8.67 0 0 1 2.1-8.47 8.23 8.23 0 0 1 2.82-2.07 41.75 41.75 0 1 1 81.3-.12 8.27 8.27 0 0 1 3.11 2.19 8.7 8.7 0 0 1 2.1 8.47c.52.78.93 1.66 1.18 2.61a8.61 8.61 0 0 1-.32 5.63Z"></path><path fill="#FFD21E" d="M47.21 76.5a34.75 34.75 0 1 0 0-69.5 34.75 34.75 0 0 0 0 69.5Z"></path><path fill="#FF9D0B" d="M81.96 41.75a34.75 34.75 0 1 0-69.5 0 34.75 34.75 0 0 0 69.5 0Zm-73.5 0a38.75 38.75 0 1 1 77.5 0 38.75 38.75 0 0 1-77.5 0Z"></path><path fill="#3A3B45" d="M58.5 32.3c1.28.44 1.78 3.06 3.07 2.38a5 5 0 1 0-6.76-2.07c.61 1.15 2.55-.72 3.7-.32ZM34.95 32.3c-1.28.44-1.79 3.06-3.07 2.38a5 5 0 1 1 6.76-2.07c-.61 1.15-2.56-.72-3.7-.32Z"></path><path fill="#FF323D" d="M46.96 56.29c9.83 0 13-8.76 13-13.26 0-2.34-1.57-1.6-4.09-.36-2.33 1.15-5.46 2.74-8.9 2.74-7.19 0-13-6.88-13-2.38s3.16 13.26 13 13.26Z"></path><path fill="#3A3B45" fill-rule="evenodd" d="M39.43 54a8.7 8.7 0 0 1 5.3-4.49c.4-.12.81.57 1.24 1.28.4.68.82 1.37 1.24 1.37.45 0 .9-.68 1.33-1.35.45-.7.89-1.38 1.32-1.25a8.61 8.61 0 0 1 5 4.17c3.73-2.94 5.1-7.74 5.1-10.7 0-2.34-1.57-1.6-4.09-.36l-.14.07c-2.31 1.15-5.39 2.67-8.77 2.67s-6.45-1.52-8.77-2.67c-2.6-1.29-4.23-2.1-4.23.29 0 3.05 1.46 8.06 5.47 10.97Z" clip-rule="evenodd"></path><path fill="#FF9D0B" d="M70.71 37a3.25 3.25 0 1 0 0-6.5 3.25 3.25 0 0 0 0 6.5ZM24.21 37a3.25 3.25 0 1 0 0-6.5 3.25 3.25 0 0 0 0 6.5ZM17.52 48c-1.62 0-3.06.66-4.07 1.87a5.97 5.97 0 0 0-1.33 3.76 7.1 7.1 0 0 0-1.94-.3c-1.55 0-2.95.59-3.94 1.66a5.8 5.8 0 0 0-.8 7 5.3 5.3 0 0 0-1.79 2.82c-.24.9-.48 2.8.8 4.74a5.22 5.22 0 0 0-.37 5.02c1.02 2.32 3.57 4.14 8.52 6.1 3.07 1.22 5.89 2 5.91 2.01a44.33 44.33 0 0 0 10.93 1.6c5.86 0 10.05-1.8 12.46-5.34 3.88-5.69 3.33-10.9-1.7-15.92-2.77-2.78-4.62-6.87-5-7.77-.78-2.66-2.84-5.62-6.25-5.62a5.7 5.7 0 0 0-4.6 2.46c-1-1.26-1.98-2.25-2.86-2.82A7.4 7.4 0 0 0 17.52 48Zm0 4c.51 0 1.14.22 1.82.65 2.14 1.36 6.25 8.43 7.76 11.18.5.92 1.37 1.31 2.14 1.31 1.55 0 2.75-1.53.15-3.48-3.92-2.93-2.55-7.72-.68-8.01.08-.02.17-.02.24-.02 1.7 0 2.45 2.93 2.45 2.93s2.2 5.52 5.98 9.3c3.77 3.77 3.97 6.8 1.22 10.83-1.88 2.75-5.47 3.58-9.16 3.58-3.81 0-7.73-.9-9.92-1.46-.11-.03-13.45-3.8-11.76-7 .28-.54.75-.76 1.34-.76 2.38 0 6.7 3.54 8.57 3.54.41 0 .7-.17.83-.6.79-2.85-12.06-4.05-10.98-8.17.2-.73.71-1.02 1.44-1.02 3.14 0 10.2 5.53 11.68 5.53.11 0 .2-.03.24-.1.74-1.2.33-2.04-4.9-5.2-5.21-3.16-8.88-5.06-6.8-7.33.24-.26.58-.38 1-.38 3.17 0 10.66 6.82 10.66 6.82s2.02 2.1 3.25 2.1c.28 0 .52-.1.68-.38.86-1.46-8.06-8.22-8.56-11.01-.34-1.9.24-2.85 1.31-2.85Z"></path><path fill="#FFD21E" d="M38.6 76.69c2.75-4.04 2.55-7.07-1.22-10.84-3.78-3.77-5.98-9.3-5.98-9.3s-.82-3.2-2.69-2.9c-1.87.3-3.24 5.08.68 8.01 3.91 2.93-.78 4.92-2.29 2.17-1.5-2.75-5.62-9.82-7.76-11.18-2.13-1.35-3.63-.6-3.13 2.2.5 2.79 9.43 9.55 8.56 11-.87 1.47-3.93-1.71-3.93-1.71s-9.57-8.71-11.66-6.44c-2.08 2.27 1.59 4.17 6.8 7.33 5.23 3.16 5.64 4 4.9 5.2-.75 1.2-12.28-8.53-13.36-4.4-1.08 4.11 11.77 5.3 10.98 8.15-.8 2.85-9.06-5.38-10.74-2.18-1.7 3.21 11.65 6.98 11.76 7.01 4.3 1.12 15.25 3.49 19.08-2.12Z"></path><path fill="#FF9D0B" d="M77.4 48c1.62 0 3.07.66 4.07 1.87a5.97 5.97 0 0 1 1.33 3.76 7.1 7.1 0 0 1 1.95-.3c1.55 0 2.95.59 3.94 1.66a5.8 5.8 0 0 1 .8 7 5.3 5.3 0 0 1 1.78 2.82c.24.9.48 2.8-.8 4.74a5.22 5.22 0 0 1 .37 5.02c-1.02 2.32-3.57 4.14-8.51 6.1-3.08 1.22-5.9 2-5.92 2.01a44.33 44.33 0 0 1-10.93 1.6c-5.86 0-10.05-1.8-12.46-5.34-3.88-5.69-3.33-10.9 1.7-15.92 2.78-2.78 4.63-6.87 5.01-7.77.78-2.66 2.83-5.62 6.24-5.62a5.7 5.7 0 0 1 4.6 2.46c1-1.26 1.98-2.25 2.87-2.82A7.4 7.4 0 0 1 77.4 48Zm0 4c-.51 0-1.13.22-1.82.65-2.13 1.36-6.25 8.43-7.76 11.18a2.43 2.43 0 0 1-2.14 1.31c-1.54 0-2.75-1.53-.14-3.48 3.91-2.93 2.54-7.72.67-8.01a1.54 1.54 0 0 0-.24-.02c-1.7 0-2.45 2.93-2.45 2.93s-2.2 5.52-5.97 9.3c-3.78 3.77-3.98 6.8-1.22 10.83 1.87 2.75 5.47 3.58 9.15 3.58 3.82 0 7.73-.9 9.93-1.46.1-.03 13.45-3.8 11.76-7-.29-.54-.75-.76-1.34-.76-2.38 0-6.71 3.54-8.57 3.54-.42 0-.71-.17-.83-.6-.8-2.85 12.05-4.05 10.97-8.17-.19-.73-.7-1.02-1.44-1.02-3.14 0-10.2 5.53-11.68 5.53-.1 0-.19-.03-.23-.1-.74-1.2-.34-2.04 4.88-5.2 5.23-3.16 8.9-5.06 6.8-7.33-.23-.26-.57-.38-.98-.38-3.18 0-10.67 6.82-10.67 6.82s-2.02 2.1-3.24 2.1a.74.74 0 0 1-.68-.38c-.87-1.46 8.05-8.22 8.55-11.01.34-1.9-.24-2.85-1.31-2.85Z"></path><path fill="#FFD21E" d="M56.33 76.69c-2.75-4.04-2.56-7.07 1.22-10.84 3.77-3.77 5.97-9.3 5.97-9.3s.82-3.2 2.7-2.9c1.86.3 3.23 5.08-.68 8.01-3.92 2.93.78 4.92 2.28 2.17 1.51-2.75 5.63-9.82 7.76-11.18 2.13-1.35 3.64-.6 3.13 2.2-.5 2.79-9.42 9.55-8.55 11 .86 1.47 3.92-1.71 3.92-1.71s9.58-8.71 11.66-6.44c2.08 2.27-1.58 4.17-6.8 7.33-5.23 3.16-5.63 4-4.9 5.2.75 1.2 12.28-8.53 13.36-4.4 1.08 4.11-11.76 5.3-10.97 8.15.8 2.85 9.05-5.38 10.74-2.18 1.69 3.21-11.65 6.98-11.76 7.01-4.31 1.12-15.26 3.49-19.08-2.12Z"></path></svg>

	

	<span>Datasets</span>
	

	</div></a><div class="relative inline-block ">
	<button class="group mr-1 mb-1 md:mr-1.5 md:mb-1.5  rounded-lg rounded-br-none " type="button">
		<div class="tag tag-white   relative rounded-br-none pr-2.5"><svg class="text-black inline-block text-sm" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" fill="none" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M22.2812 12.2656L25.9532 15.7187C26.8932 16.6587 28.0913 17.3931 29.0313 16.4531C29.8594 15.7812 29.9332 14.1 29.9532 13.5C29.9532 11.5625 28.9219 8.375 27.25 6.71875C25.5604 5.04493 23.3782 3.91692 22.7032 3.78125L22.2812 12.2656Z" fill="#F5AB6A"></path><path d="M22.2812 12.2656L25.9532 15.7187C26.8932 16.6587 28.0913 17.3931 29.0313 16.4531C29.8594 15.7812 29.9332 14.1 29.9532 13.5C29.9532 11.5625 28.9219 8.375 27.25 6.71875C25.5604 5.04493 23.3782 3.91692 22.7032 3.78125L22.2812 12.2656Z" fill="url(#paint0_radial_18_31665)"></path><g filter="url(#filter0_f_18_31665)"><path d="M22.2849 12.1817L23.4375 13.2656L24.4375 4.70312C23.5121 4.1242 23.0198 3.96369 22.6563 3.89062L22.2849 12.1817Z" fill="url(#paint1_linear_18_31665)"></path></g><path d="M22.7969 3.05741L21.8437 2.65269C19.6421 1.96765 17.2344 1.81208 14.6719 2.23236C12.1094 2.65264 11.5156 3.2442 11.5156 3.2442C10.896 3.3674 10.8671 3.88898 11.1718 4.45363C13.0797 6.72576 15.176 13.4043 18.0469 14.2506C18.89 14.4662 21.3791 14.4776 22.2019 14.1593L22.3238 14.108C22.6692 13.9745 23.1672 13.2814 23.1875 12.9118L23.4219 4.03043C23.4523 3.59924 23.1484 3.25204 22.7969 3.05741Z" fill="url(#paint2_radial_18_31665)"></path><path d="M22.7969 3.05741L21.8437 2.65269C19.6421 1.96765 17.2344 1.81208 14.6719 2.23236C12.1094 2.65264 11.5156 3.2442 11.5156 3.2442C10.896 3.3674 10.8671 3.88898 11.1718 4.45363C13.0797 6.72576 15.176 13.4043 18.0469 14.2506C18.89 14.4662 21.3791 14.4776 22.2019 14.1593L22.3238 14.108C22.6692 13.9745 23.1672 13.2814 23.1875 12.9118L23.4219 4.03043C23.4523 3.59924 23.1484 3.25204 22.7969 3.05741Z" fill="url(#paint3_radial_18_31665)"></path><path d="M22.7969 3.05741L21.8437 2.65269C19.6421 1.96765 17.2344 1.81208 14.6719 2.23236C12.1094 2.65264 11.5156 3.2442 11.5156 3.2442C10.896 3.3674 10.8671 3.88898 11.1718 4.45363C13.0797 6.72576 15.176 13.4043 18.0469 14.2506C18.89 14.4662 21.3791 14.4776 22.2019 14.1593L22.3238 14.108C22.6692 13.9745 23.1672 13.2814 23.1875 12.9118L23.4219 4.03043C23.4523 3.59924 23.1484 3.25204 22.7969 3.05741Z" fill="url(#paint4_radial_18_31665)"></path><path d="M22.7969 3.05741L21.8437 2.65269C19.6421 1.96765 17.2344 1.81208 14.6719 2.23236C12.1094 2.65264 11.5156 3.2442 11.5156 3.2442C10.896 3.3674 10.8671 3.88898 11.1718 4.45363C13.0797 6.72576 15.176 13.4043 18.0469 14.2506C18.89 14.4662 21.3791 14.4776 22.2019 14.1593L22.3238 14.108C22.6692 13.9745 23.1672 13.2814 23.1875 12.9118L23.4219 4.03043C23.4523 3.59924 23.1484 3.25204 22.7969 3.05741Z" fill="url(#paint5_radial_18_31665)"></path><path d="M22.7969 3.05741L21.8437 2.65269C19.6421 1.96765 17.2344 1.81208 14.6719 2.23236C12.1094 2.65264 11.5156 3.2442 11.5156 3.2442C10.896 3.3674 10.8671 3.88898 11.1718 4.45363C13.0797 6.72576 15.176 13.4043 18.0469 14.2506C18.89 14.4662 21.3791 14.4776 22.2019 14.1593L22.3238 14.108C22.6692 13.9745 23.1672 13.2814 23.1875 12.9118L23.4219 4.03043C23.4523 3.59924 23.1484 3.25204 22.7969 3.05741Z" fill="url(#paint6_linear_18_31665)"></path><g filter="url(#filter1_f_18_31665)"><path d="M13.1016 2.72656C11.862 3.06924 11.5298 3.40016 11.5298 3.40016C10.9102 3.52335 10.936 4.11525 11.2408 4.6799C13.1487 6.95202 15.1361 13.2496 18.007 14.0958C18.2707 14.1633 18.6953 14.2107 19.1797 14.2344L13.1016 2.72656Z" fill="url(#paint7_linear_18_31665)"></path></g><path d="M12.2187 22.7187L15.7656 26.2031C16.7332 27.1171 17.3334 28.2487 16.4219 29.2188C15.7749 30.0687 14.2241 29.9933 13.625 30.0313C11.6883 30.0891 9.09014 29.5622 6.84373 27.5313C5.07737 25.9343 4.09321 23.688 3.93751 23.0156L12.2187 22.7187Z" fill="url(#paint8_radial_18_31665)"></path><path d="M12.2187 22.7187L15.7656 26.2031C16.7332 27.1171 17.3334 28.2487 16.4219 29.2188C15.7749 30.0687 14.2241 29.9933 13.625 30.0313C11.6883 30.0891 9.09014 29.5622 6.84373 27.5313C5.07737 25.9343 4.09321 23.688 3.93751 23.0156L12.2187 22.7187Z" fill="url(#paint9_radial_18_31665)"></path><g filter="url(#filter2_f_18_31665)"><path d="M12.0523 22.7916L13.2187 23.9375L4.81018 24.5721C4.4328 23.8671 4.20835 23.2768 4.14062 22.9844L12.0523 22.7916Z" fill="url(#paint10_linear_18_31665)"></path><path d="M12.0523 22.7916L13.2187 23.9375L4.81018 24.5721C4.4328 23.8671 4.20835 23.2768 4.14062 22.9844L12.0523 22.7916Z" fill="url(#paint11_radial_18_31665)"></path></g><path d="M2.99219 22.6484C2.07068 20.538 1.78913 17.4452 2.21096 15.0703C2.63279 12.6953 3.20759 11.951 3.20759 11.951C3.31231 11.3264 3.83281 11.2818 4.40626 11.5703C6.73409 13.4144 13.3119 15.2264 14.2432 18.0781C14.5947 19.3034 14.6279 21.3125 14.1641 22.5156C14.0409 22.8657 13.5 23.3516 13.0625 23.4141C12.625 23.4765 9.47656 23.3516 8.61719 23.3516C7.75781 23.3516 4.64844 23.6719 4.14062 23.6172C3.63281 23.5625 3.23437 23.2031 2.99219 22.6484Z" fill="#EC9F6A"></path><path d="M2.99219 22.6484C2.07068 20.538 1.78913 17.4452 2.21096 15.0703C2.63279 12.6953 3.20759 11.951 3.20759 11.951C3.31231 11.3264 3.83281 11.2818 4.40626 11.5703C6.73409 13.4144 13.3119 15.2264 14.2432 18.0781C14.5947 19.3034 14.6279 21.3125 14.1641 22.5156C14.0409 22.8657 13.5 23.3516 13.0625 23.4141C12.625 23.4765 9.47656 23.3516 8.61719 23.3516C7.75781 23.3516 4.64844 23.6719 4.14062 23.6172C3.63281 23.5625 3.23437 23.2031 2.99219 22.6484Z" fill="url(#paint12_radial_18_31665)"></path><path d="M2.99219 22.6484C2.07068 20.538 1.78913 17.4452 2.21096 15.0703C2.63279 12.6953 3.20759 11.951 3.20759 11.951C3.31231 11.3264 3.83281 11.2818 4.40626 11.5703C6.73409 13.4144 13.3119 15.2264 14.2432 18.0781C14.5947 19.3034 14.6279 21.3125 14.1641 22.5156C14.0409 22.8657 13.5 23.3516 13.0625 23.4141C12.625 23.4765 9.47656 23.3516 8.61719 23.3516C7.75781 23.3516 4.64844 23.6719 4.14062 23.6172C3.63281 23.5625 3.23437 23.2031 2.99219 22.6484Z" fill="url(#paint13_linear_18_31665)"></path><path d="M2.99219 22.6484C2.07068 20.538 1.78913 17.4452 2.21096 15.0703C2.63279 12.6953 3.20759 11.951 3.20759 11.951C3.31231 11.3264 3.83281 11.2818 4.40626 11.5703C6.73409 13.4144 13.3119 15.2264 14.2432 18.0781C14.5947 19.3034 14.6279 21.3125 14.1641 22.5156C14.0409 22.8657 13.5 23.3516 13.0625 23.4141C12.625 23.4765 9.47656 23.3516 8.61719 23.3516C7.75781 23.3516 4.64844 23.6719 4.14062 23.6172C3.63281 23.5625 3.23437 23.2031 2.99219 22.6484Z" fill="url(#paint14_radial_18_31665)"></path><path d="M2.99219 22.6484C2.07068 20.538 1.78913 17.4452 2.21096 15.0703C2.63279 12.6953 3.20759 11.951 3.20759 11.951C3.31231 11.3264 3.83281 11.2818 4.40626 11.5703C6.73409 13.4144 13.3119 15.2264 14.2432 18.0781C14.5947 19.3034 14.6279 21.3125 14.1641 22.5156C14.0409 22.8657 13.5 23.3516 13.0625 23.4141C12.625 23.4765 9.47656 23.3516 8.61719 23.3516C7.75781 23.3516 4.64844 23.6719 4.14062 23.6172C3.63281 23.5625 3.23437 23.2031 2.99219 22.6484Z" fill="url(#paint15_radial_18_31665)"></path><path d="M2.99219 22.6484C2.07068 20.538 1.78913 17.4452 2.21096 15.0703C2.63279 12.6953 3.20759 11.951 3.20759 11.951C3.31231 11.3264 3.83281 11.2818 4.40626 11.5703C6.73409 13.4144 13.3119 15.2264 14.2432 18.0781C14.5947 19.3034 14.6279 21.3125 14.1641 22.5156C14.0409 22.8657 13.5 23.3516 13.0625 23.4141C12.625 23.4765 9.47656 23.3516 8.61719 23.3516C7.75781 23.3516 4.64844 23.6719 4.14062 23.6172C3.63281 23.5625 3.23437 23.2031 2.99219 22.6484Z" fill="url(#paint16_radial_18_31665)"></path><g filter="url(#filter3_f_18_31665)"><path d="M2.70313 13.6719C3.04135 12.4711 3.36224 12.0555 3.36224 12.0555C3.46697 11.4309 3.98746 11.3864 4.56092 11.6749C6.88874 13.5189 13.0809 15.1104 14.0121 17.9622C14.1731 18.5231 14.2766 19.0394 14.3287 19.5128L2.70313 13.6719Z" fill="url(#paint17_linear_18_31665)"></path><path d="M2.70313 13.6719C3.04135 12.4711 3.36224 12.0555 3.36224 12.0555C3.46697 11.4309 3.98746 11.3864 4.56092 11.6749C6.88874 13.5189 13.0809 15.1104 14.0121 17.9622C14.1731 18.5231 14.2766 19.0394 14.3287 19.5128L2.70313 13.6719Z" fill="url(#paint18_linear_18_31665)"></path></g><path d="M9.83184 2.82184C6.62184 4.07184 4.07184 6.62184 2.82184 9.83184C2.48184 10.7118 2.82184 11.7018 3.62184 12.1918L14.0418 18.5418C14.6618 18.9218 15.4418 18.9218 16.0618 18.5418C17.0718 17.9218 17.9318 17.0718 18.5418 16.0618C18.9218 15.4418 18.9218 14.6618 18.5418 14.0418L12.1918 3.62184C11.7018 2.82184 10.7118 2.48184 9.83184 2.82184Z" fill="#D79453"></path><path d="M9.83184 2.82184C6.62184 4.07184 4.07184 6.62184 2.82184 9.83184C2.48184 10.7118 2.82184 11.7018 3.62184 12.1918L14.0418 18.5418C14.6618 18.9218 15.4418 18.9218 16.0618 18.5418C17.0718 17.9218 17.9318 17.0718 18.5418 16.0618C18.9218 15.4418 18.9218 14.6618 18.5418 14.0418L12.1918 3.62184C11.7018 2.82184 10.7118 2.48184 9.83184 2.82184Z" fill="url(#paint19_radial_18_31665)"></path><path d="M9.83184 2.82184C6.62184 4.07184 4.07184 6.62184 2.82184 9.83184C2.48184 10.7118 2.82184 11.7018 3.62184 12.1918L14.0418 18.5418C14.6618 18.9218 15.4418 18.9218 16.0618 18.5418C17.0718 17.9218 17.9318 17.0718 18.5418 16.0618C18.9218 15.4418 18.9218 14.6618 18.5418 14.0418L12.1918 3.62184C11.7018 2.82184 10.7118 2.48184 9.83184 2.82184Z" fill="url(#paint20_radial_18_31665)"></path><path d="M9.83184 2.82184C6.62184 4.07184 4.07184 6.62184 2.82184 9.83184C2.48184 10.7118 2.82184 11.7018 3.62184 12.1918L14.0418 18.5418C14.6618 18.9218 15.4418 18.9218 16.0618 18.5418C17.0718 17.9218 17.9318 17.0718 18.5418 16.0618C18.9218 15.4418 18.9218 14.6618 18.5418 14.0418L12.1918 3.62184C11.7018 2.82184 10.7118 2.48184 9.83184 2.82184Z" fill="url(#paint21_radial_18_31665)"></path><path d="M9.83184 2.82184C6.62184 4.07184 4.07184 6.62184 2.82184 9.83184C2.48184 10.7118 2.82184 11.7018 3.62184 12.1918L14.0418 18.5418C14.6618 18.9218 15.4418 18.9218 16.0618 18.5418C17.0718 17.9218 17.9318 17.0718 18.5418 16.0618C18.9218 15.4418 18.9218 14.6618 18.5418 14.0418L12.1918 3.62184C11.7018 2.82184 10.7118 2.48184 9.83184 2.82184Z" fill="url(#paint22_linear_18_31665)"></path><path d="M9.83184 2.82184C6.62184 4.07184 4.07184 6.62184 2.82184 9.83184C2.48184 10.7118 2.82184 11.7018 3.62184 12.1918L14.0418 18.5418C14.6618 18.9218 15.4418 18.9218 16.0618 18.5418C17.0718 17.9218 17.9318 17.0718 18.5418 16.0618C18.9218 15.4418 18.9218 14.6618 18.5418 14.0418L12.1918 3.62184C11.7018 2.82184 10.7118 2.48184 9.83184 2.82184Z" fill="url(#paint23_radial_18_31665)"></path><path d="M9.83184 2.82184C6.62184 4.07184 4.07184 6.62184 2.82184 9.83184C2.48184 10.7118 2.82184 11.7018 3.62184 12.1918L14.0418 18.5418C14.6618 18.9218 15.4418 18.9218 16.0618 18.5418C17.0718 17.9218 17.9318 17.0718 18.5418 16.0618C18.9218 15.4418 18.9218 14.6618 18.5418 14.0418L12.1918 3.62184C11.7018 2.82184 10.7118 2.48184 9.83184 2.82184Z" fill="url(#paint24_radial_18_31665)"></path><defs><filter id="filter0_f_18_31665" x="22.0349" y="3.64062" width="2.65265" height="9.875" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood><feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"></feBlend><feGaussianBlur stdDeviation="0.125" result="effect1_foregroundBlur_18_31665"></feGaussianBlur></filter><filter id="filter1_f_18_31665" x="10.7815" y="2.47656" width="8.64819" height="12.0078" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood><feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"></feBlend><feGaussianBlur stdDeviation="0.125" result="effect1_foregroundBlur_18_31665"></feGaussianBlur></filter><filter id="filter2_f_18_31665" x="3.89062" y="22.5416" width="9.57812" height="2.2804" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood><feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"></feBlend><feGaussianBlur stdDeviation="0.125" result="effect1_foregroundBlur_18_31665"></feGaussianBlur></filter><filter id="filter3_f_18_31665" x="2.45312" y="11.2538" width="12.1255" height="8.50903" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood><feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"></feBlend><feGaussianBlur stdDeviation="0.125" result="effect1_foregroundBlur_18_31665"></feGaussianBlur></filter><radialGradient id="paint0_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(22.8125 12.9375) rotate(42.7741) scale(12.5164 7.08839)"><stop offset="0.0937591" stop-color="#C05159"></stop><stop offset="0.553697" stop-color="#F6AC6A"></stop><stop offset="0.832916" stop-color="#FFD186"></stop><stop offset="0.916927" stop-color="#FFDC87"></stop></radialGradient><linearGradient id="paint1_linear_18_31665" x1="24.7344" y1="4.67187" x2="20.8594" y2="12.8906" gradientUnits="userSpaceOnUse"><stop stop-color="#EBD67C"></stop><stop offset="0.0655686" stop-color="#FFFFA6"></stop><stop offset="0.530552" stop-color="#F8C281"></stop><stop offset="0.937338" stop-color="#E99E6B"></stop></linearGradient><radialGradient id="paint2_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(22.9009 13.1847) rotate(-127.648) scale(14.3438 11.7966)"><stop stop-color="#FFBE66"></stop><stop offset="1" stop-color="#E2AE5B"></stop></radialGradient><radialGradient id="paint3_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(18 11.4375) rotate(53.9726) scale(11.9013 4.84018)"><stop stop-color="#D67C63"></stop><stop offset="1" stop-color="#D97D67" stop-opacity="0"></stop></radialGradient><radialGradient id="paint4_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(23 4.1875) rotate(45.7639) scale(3.31486 5.75622)"><stop stop-color="#FFE4A6"></stop><stop offset="0.711285" stop-color="#F8B76F"></stop><stop offset="1" stop-color="#F9B870" stop-opacity="0"></stop></radialGradient><radialGradient id="paint5_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(22.875 12.4375) rotate(88.9391) scale(3.37558 1.29066)"><stop stop-color="#FFBC67"></stop><stop offset="1" stop-color="#FFBC67" stop-opacity="0"></stop></radialGradient><linearGradient id="paint6_linear_18_31665" x1="20.375" y1="15.6875" x2="20.125" y2="12.7813" gradientUnits="userSpaceOnUse"><stop offset="0.461609" stop-color="#B45077"></stop><stop offset="0.855389" stop-color="#B75077" stop-opacity="0"></stop></linearGradient><linearGradient id="paint7_linear_18_31665" x1="12.9375" y1="2.57056" x2="18.5625" y2="14.3891" gradientUnits="userSpaceOnUse"><stop stop-color="#DDC173"></stop><stop offset="0.485173" stop-color="#D59F65"></stop><stop offset="1" stop-color="#E49966"></stop></linearGradient><radialGradient id="paint8_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(13.5625 23.5) rotate(109.113) scale(6.68078 10.2578)"><stop offset="0.165756" stop-color="#FFBF7E"></stop><stop offset="0.827674" stop-color="#DF8C6D"></stop><stop offset="1" stop-color="#B05A66"></stop></radialGradient><radialGradient id="paint9_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(15.1875 26) rotate(41.0652) scale(8.37243 2.03649)"><stop stop-color="#FFD483"></stop><stop offset="1" stop-color="#FFD688" stop-opacity="0"></stop></radialGradient><linearGradient id="paint10_linear_18_31665" x1="3.96063" y1="23.794" x2="13.3748" y2="23.5143" gradientUnits="userSpaceOnUse"><stop stop-color="#A8716F"></stop><stop offset="0.103615" stop-color="#B37173"></stop><stop offset="0.225484" stop-color="#DB9F84"></stop><stop offset="0.799889" stop-color="#F1BB8A"></stop><stop offset="1" stop-color="#FFD780"></stop></linearGradient><radialGradient id="paint11_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(11.4219 23.1719) rotate(-178.616) scale(3.23532 0.569081)"><stop offset="0.621498" stop-color="#AF5A3E"></stop><stop offset="1" stop-color="#B35445" stop-opacity="0"></stop></radialGradient><radialGradient id="paint12_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(13.625 19.125) rotate(-171.737) scale(15.2205 15.0767)"><stop offset="0.138435" stop-color="#FFB974"></stop><stop offset="0.403618" stop-color="#F2A56D"></stop><stop offset="0.925938" stop-color="#A16948"></stop></radialGradient><linearGradient id="paint13_linear_18_31665" x1="8.22184" y1="13.125" x2="6.81191" y2="15.4996" gradientUnits="userSpaceOnUse"><stop offset="0.610751" stop-color="#984847"></stop><stop offset="0.850075" stop-color="#9A4947" stop-opacity="0"></stop></linearGradient><radialGradient id="paint14_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(7.25 23.7461) scale(11.25 5.68361)"><stop stop-color="#C66364"></stop><stop offset="1" stop-color="#D4766B" stop-opacity="0"></stop></radialGradient><radialGradient id="paint15_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(7.875 23.5313) scale(10.0937 1.29657)"><stop stop-color="#B64B4B"></stop><stop offset="1" stop-color="#C56158" stop-opacity="0"></stop></radialGradient><radialGradient id="paint16_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(11.4375 19.875) rotate(-46.8882) scale(4.02385 7.51767)"><stop stop-color="#FFC083"></stop><stop offset="0.620218" stop-color="#FFBD7D" stop-opacity="0"></stop></radialGradient><linearGradient id="paint17_linear_18_31665" x1="2.8125" y1="13.0312" x2="14.5582" y2="18.9404" gradientUnits="userSpaceOnUse"><stop stop-color="#B89367"></stop><stop offset="1" stop-color="#C5835E"></stop></linearGradient><linearGradient id="paint18_linear_18_31665" x1="8.21875" y1="14.6406" x2="7.59349" y2="15.6717" gradientUnits="userSpaceOnUse"><stop offset="0.351552" stop-color="#A74746"></stop><stop offset="0.845198" stop-color="#A04346" stop-opacity="0"></stop></linearGradient><radialGradient id="paint19_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(15.5625 14.5625) rotate(140.244) scale(18.3733 13.7403)"><stop stop-color="#FDAE69"></stop><stop offset="0.729021" stop-color="#CE8C4F"></stop><stop offset="0.921546" stop-color="#AD7B45"></stop><stop offset="1" stop-color="#8B6B4A"></stop></radialGradient><radialGradient id="paint20_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(15.0625 7) rotate(65.3152) scale(11.0745 3.16547)"><stop offset="0.233237" stop-color="#FFD47C"></stop><stop offset="0.853648" stop-color="#FFD98B" stop-opacity="0"></stop></radialGradient><radialGradient id="paint21_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(15.3125 8.875) rotate(100.886) scale(6.6191 5.57808)"><stop offset="0.128419" stop-color="#FFD88C"></stop><stop offset="0.924134" stop-color="#FFBE7B" stop-opacity="0"></stop></radialGradient><linearGradient id="paint22_linear_18_31665" x1="7.25" y1="15.1875" x2="10.7588" y2="10.3142" gradientUnits="userSpaceOnUse"><stop offset="0.142353" stop-color="#C15F4D"></stop><stop offset="1" stop-color="#D58366" stop-opacity="0"></stop></linearGradient><radialGradient id="paint23_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(8.15625 15.7813) rotate(28.5422) scale(12.5574 1.96589)"><stop offset="0.149989" stop-color="#E4745D"></stop><stop offset="0.453292" stop-color="#C8604C"></stop><stop offset="0.632597" stop-color="#C0605F"></stop><stop offset="1" stop-color="#C0605F" stop-opacity="0"></stop></radialGradient><radialGradient id="paint24_radial_18_31665" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(1.40625 2.69067) rotate(46.0943) scale(22.3963)"><stop offset="0.935802" stop-color="#C17C61" stop-opacity="0"></stop><stop offset="0.982109" stop-color="#C17C61"></stop></radialGradient></defs></svg>

	

	<span>Croissant</span>
	

	<div class="border-br-gray-200 absolute bottom-0.5 right-0.5 h-1 w-1 border-[3px] border-l-transparent border-t-transparent border-b-gray-200 border-r-gray-200 dark:border-b-gray-700 dark:border-r-gray-700"></div></div>
		
		</button>
	
	
	</div>

	</div><div class="mr-1 flex flex-wrap items-center"><span class="mb-1 mr-1 p-1 text-sm leading-tight text-gray-400 md:mb-1.5">License:
	</span>
	<div class="relative inline-block ">
	<button class="group mr-1 mb-1 md:mr-1.5 md:mb-1.5  rounded-full rounded-br-none " type="button">
		<div class="tag tag-white rounded-full  relative rounded-br-none pr-2.5">
		<svg class="text-xs text-gray-900" width="1em" height="1em" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1.46009 5.0945V6.88125C1.46009 7.25201 1.75937 7.55129 2.13012 7.55129C2.50087 7.55129 2.80016 7.25201 2.80016 6.88125V5.0945C2.80016 4.72375 2.50087 4.42446 2.13012 4.42446C1.75937 4.42446 1.46009 4.72375 1.46009 5.0945ZM4.14022 5.0945V6.88125C4.14022 7.25201 4.4395 7.55129 4.81026 7.55129C5.18101 7.55129 5.48029 7.25201 5.48029 6.88125V5.0945C5.48029 4.72375 5.18101 4.42446 4.81026 4.42446C4.4395 4.42446 4.14022 4.72375 4.14022 5.0945ZM1.23674 9.78473H8.38377C8.75452 9.78473 9.0538 9.48545 9.0538 9.1147C9.0538 8.74395 8.75452 8.44466 8.38377 8.44466H1.23674C0.865993 8.44466 0.566711 8.74395 0.566711 9.1147C0.566711 9.48545 0.865993 9.78473 1.23674 9.78473ZM6.82036 5.0945V6.88125C6.82036 7.25201 7.11964 7.55129 7.49039 7.55129C7.86114 7.55129 8.16042 7.25201 8.16042 6.88125V5.0945C8.16042 4.72375 7.86114 4.42446 7.49039 4.42446C7.11964 4.42446 6.82036 4.72375 6.82036 5.0945ZM4.39484 0.623142L0.865993 2.48137C0.682851 2.57517 0.566711 2.76725 0.566711 2.97273C0.566711 3.28094 0.816857 3.53109 1.12507 3.53109H8.49991C8.80365 3.53109 9.0538 3.28094 9.0538 2.97273C9.0538 2.76725 8.93766 2.57517 8.75452 2.48137L5.22568 0.623142C4.9666 0.484669 4.65391 0.484669 4.39484 0.623142V0.623142Z" fill="currentColor"></path></svg>

	

	<span>cc0-1.0</span>
	

	<div class="border-br-gray-200 absolute bottom-0.5 right-0.5 h-1 w-1 border-[3px] border-l-transparent border-t-transparent border-b-gray-200 border-r-gray-200 dark:border-b-gray-700 dark:border-r-gray-700"></div></div>
		
		</button>
	
	
	</div>

	</div></div>

		<div class="flex flex-col-reverse lg:flex-row lg:items-center lg:justify-between"><div class="-mb-px flex h-12 items-center overflow-x-auto overflow-y-hidden ">
	<a class="tab-alternate" href="/datasets/mozilla-foundation/common_voice_13_0"><svg class="mr-1.5 text-gray-400 flex-none" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
	Dataset card
	

	
		</a><a class="tab-alternate" href="/datasets/mozilla-foundation/common_voice_13_0/viewer/"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 12 12"><path fill="currentColor" d="M2.5 2h7a1 1 0 0 1 1 1v6a1 1 0 0 1-1 1h-7a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1Zm0 2v2h3V4h-3Zm4 0v2h3V4h-3Zm-4 3v2h3V7h-3Zm4 0v2h3V7h-3Z"></path></svg>
	Data Studio
	

	
		</a><a class="tab-alternate active" href="/datasets/mozilla-foundation/common_voice_13_0/tree/main"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M21 19h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-8h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0 4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M9 19a1 1 0 0 1-1-1V6a1 1 0 0 1 2 0v12a1 1 0 0 1-1 1zm-6-4.333a1 1 0 0 1-.64-1.769L3.438 12l-1.078-.898a1 1 0 0 1 1.28-1.538l2 1.667a1 1 0 0 1 0 1.538l-2 1.667a.999.999 0 0 1-.64.231z" fill="currentColor"></path></svg>
	<span class="xl:hidden">Files</span>
		<span class="hidden xl:inline">Files and versions</span>
	

	
		</a><a class="tab-alternate" href="/datasets/mozilla-foundation/common_voice_13_0/discussions"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M20.6081 3C21.7684 3 22.8053 3.49196 23.5284 4.38415C23.9756 4.93678 24.4428 5.82749 24.4808 7.16133C24.9674 7.01707 25.4353 6.93643 25.8725 6.93643C26.9833 6.93643 27.9865 7.37587 28.696 8.17411C29.6075 9.19872 30.0124 10.4579 29.8361 11.7177C29.7523 12.3177 29.5581 12.8555 29.2678 13.3534C29.8798 13.8646 30.3306 14.5763 30.5485 15.4322C30.719 16.1032 30.8939 17.5006 29.9808 18.9403C30.0389 19.0342 30.0934 19.1319 30.1442 19.2318C30.6932 20.3074 30.7283 21.5229 30.2439 22.6548C29.5093 24.3704 27.6841 25.7219 24.1397 27.1727C21.9347 28.0753 19.9174 28.6523 19.8994 28.6575C16.9842 29.4379 14.3477 29.8345 12.0653 29.8345C7.87017 29.8345 4.8668 28.508 3.13831 25.8921C0.356375 21.6797 0.754104 17.8269 4.35369 14.1131C6.34591 12.058 7.67023 9.02782 7.94613 8.36275C8.50224 6.39343 9.97271 4.20438 12.4172 4.20438H12.4179C12.6236 4.20438 12.8314 4.2214 13.0364 4.25468C14.107 4.42854 15.0428 5.06476 15.7115 6.02205C16.4331 5.09583 17.134 4.359 17.7682 3.94323C18.7242 3.31737 19.6794 3 20.6081 3ZM20.6081 5.95917C20.2427 5.95917 19.7963 6.1197 19.3039 6.44225C17.7754 7.44319 14.8258 12.6772 13.7458 14.7131C13.3839 15.3952 12.7655 15.6837 12.2086 15.6837C11.1036 15.6837 10.2408 14.5497 12.1076 13.1085C14.9146 10.9402 13.9299 7.39584 12.5898 7.1776C12.5311 7.16799 12.4731 7.16355 12.4172 7.16355C11.1989 7.16355 10.6615 9.33114 10.6615 9.33114C10.6615 9.33114 9.0863 13.4148 6.38031 16.206C3.67434 18.998 3.5346 21.2388 5.50675 24.2246C6.85185 26.2606 9.42666 26.8753 12.0653 26.8753C14.8021 26.8753 17.6077 26.2139 19.1799 25.793C19.2574 25.7723 28.8193 22.984 27.6081 20.6107C27.4046 20.212 27.0693 20.0522 26.6471 20.0522C24.9416 20.0522 21.8393 22.6726 20.5057 22.6726C20.2076 22.6726 19.9976 22.5416 19.9116 22.222C19.3433 20.1173 28.552 19.2325 27.7758 16.1839C27.639 15.6445 27.2677 15.4256 26.746 15.4263C24.4923 15.4263 19.4358 19.5181 18.3759 19.5181C18.2949 19.5181 18.2368 19.4937 18.2053 19.4419C17.6743 18.557 17.9653 17.9394 21.7082 15.6009C25.4511 13.2617 28.0783 11.8545 26.5841 10.1752C26.4121 9.98141 26.1684 9.8956 25.8725 9.8956C23.6001 9.89634 18.2311 14.9403 18.2311 14.9403C18.2311 14.9403 16.7821 16.496 15.9057 16.496C15.7043 16.496 15.533 16.4139 15.4169 16.2112C14.7956 15.1296 21.1879 10.1286 21.5484 8.06535C21.7928 6.66715 21.3771 5.95917 20.6081 5.95917Z" fill="#FF9D00"></path><path d="M5.50686 24.2246C3.53472 21.2387 3.67446 18.9979 6.38043 16.206C9.08641 13.4147 10.6615 9.33111 10.6615 9.33111C10.6615 9.33111 11.2499 6.95933 12.59 7.17757C13.93 7.39581 14.9139 10.9401 12.1069 13.1084C9.29997 15.276 12.6659 16.7489 13.7459 14.713C14.8258 12.6772 17.7747 7.44316 19.304 6.44221C20.8326 5.44128 21.9089 6.00204 21.5484 8.06532C21.188 10.1286 14.795 15.1295 15.4171 16.2118C16.0391 17.2934 18.2312 14.9402 18.2312 14.9402C18.2312 14.9402 25.0907 8.49588 26.5842 10.1752C28.0776 11.8545 25.4512 13.2616 21.7082 15.6008C17.9646 17.9393 17.6744 18.557 18.2054 19.4418C18.7372 20.3266 26.9998 13.1351 27.7759 16.1838C28.5513 19.2324 19.3434 20.1173 19.9117 22.2219C20.48 24.3274 26.3979 18.2382 27.6082 20.6107C28.8193 22.9839 19.2574 25.7722 19.18 25.7929C16.0914 26.62 8.24723 28.3726 5.50686 24.2246Z" fill="#FFD21E"></path></svg>
	Community
	<div class="ml-1.5 flex h-4 min-w-[1rem] items-center justify-center rounded px-1 text-xs leading-none shadow-sm bg-black text-white dark:bg-gray-800 dark:text-gray-200">9</div>

	
		</a></div>
	
			</div></div></header>


</div>
	
<div class="container relative flex flex-col md:grid md:space-y-0 w-full md:grid-cols-12  space-y-4 md:gap-6 mb-16"><section class="pt-8 border-gray-100 col-span-full"><header class="flex flex-wrap items-center justify-start pb-2 md:justify-end lg:flex-nowrap"><div class="grow max-md:flex max-md:w-full max-md:items-start max-md:justify-between"><div class="relative mr-4 flex min-w-0 basis-auto flex-wrap items-center md:grow md:basis-full lg:basis-auto lg:flex-nowrap"><div class="SVELTE_HYDRATER contents" data-target="BranchSelector" data-props="{&quot;path&quot;:&quot;README.md&quot;,&quot;repoName&quot;:&quot;mozilla-foundation/common_voice_13_0&quot;,&quot;repoType&quot;:&quot;dataset&quot;,&quot;rev&quot;:&quot;main&quot;,&quot;refs&quot;:{&quot;branches&quot;:[{&quot;name&quot;:&quot;main&quot;,&quot;ref&quot;:&quot;refs/heads/main&quot;,&quot;targetCommit&quot;:&quot;8c6ec32c340031124236862abfed7be1583d1172&quot;}],&quot;tags&quot;:[],&quot;converts&quot;:[{&quot;name&quot;:&quot;duckdb&quot;,&quot;ref&quot;:&quot;refs/convert/duckdb&quot;,&quot;targetCommit&quot;:&quot;fdc4dc69e510ba6e85110b402dc713cb73f0233c&quot;},{&quot;name&quot;:&quot;parquet&quot;,&quot;ref&quot;:&quot;refs/convert/parquet&quot;,&quot;targetCommit&quot;:&quot;437b721889a62d1dab88950395f3059456dea922&quot;}]},&quot;view&quot;:&quot;blob&quot;}"><div class="relative mr-4 mb-2">
	<button class="text-sm md:text-base btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 text-gray-700 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M13 14c-3.36 0-4.46 1.35-4.82 2.24C9.25 16.7 10 17.76 10 19a3 3 0 0 1-3 3a3 3 0 0 1-3-3c0-1.31.83-2.42 2-2.83V7.83A2.99 2.99 0 0 1 4 5a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.31-.83 2.42-2 2.83v5.29c.88-.65 2.16-1.12 4-1.12c2.67 0 3.56-1.34 3.85-2.23A3.006 3.006 0 0 1 14 7a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.34-.88 2.5-2.09 2.86C17.65 11.29 16.68 14 13 14m-6 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1M7 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1m10 2a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1z" fill="currentColor"></path></svg>
			main
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div></div>
			<div class="relative mb-2 flex flex-wrap items-center"><a class="truncate text-gray-800 hover:underline" href="/datasets/mozilla-foundation/common_voice_13_0/tree/main">common_voice_13_0</a>
				<span class="mx-1 text-gray-300">/</span>
					<span class="dark:text-gray-300">README.md</span>
					<div class="SVELTE_HYDRATER contents" data-target="CopyButton" data-props="{&quot;value&quot;:&quot;README.md&quot;,&quot;classNames&quot;:&quot;text-xs ml-2&quot;,&quot;title&quot;:&quot;Copy path&quot;}"><button class="relative text-xs ml-2 focus:outline-hidden inline-flex cursor-pointer items-center text-sm  mx-0.5   text-gray-600 " title="Copy path" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	</button></div></div></div>
		</div>
	
	</header>
			<div class="SVELTE_HYDRATER contents" data-target="LastCommit" data-props="{&quot;commitLast&quot;:{&quot;date&quot;:&quot;2023-03-30T09:29:31.000Z&quot;,&quot;subject&quot;:&quot;Update README.md&quot;,&quot;authors&quot;:[{&quot;_id&quot;:&quot;61b85ce86eb1f2c5e6233736&quot;,&quot;avatar&quot;:&quot;https://cdn-avatars.huggingface.co/v1/production/uploads/1655385361868-61b85ce86eb1f2c5e6233736.jpeg&quot;,&quot;isHf&quot;:true,&quot;user&quot;:&quot;reach-vb&quot;}],&quot;commit&quot;:{&quot;id&quot;:&quot;34e1cfbb8f95ea840cc84c1975e4a4088d810ce5&quot;,&quot;parentIds&quot;:[&quot;9b1a64f080c569ff1c6460260a1bc1de18d79caa&quot;]},&quot;title&quot;:&quot;Update README.md&quot;},&quot;repo&quot;:{&quot;name&quot;:&quot;mozilla-foundation/common_voice_13_0&quot;,&quot;type&quot;:&quot;dataset&quot;}}"><div class="from-gray-100-to-white bg-linear-to-t flex flex-wrap items-baseline rounded-t-lg border border-b-0 px-3 py-2 dark:border-gray-800"><img class="mr-2.5 mt-0.5 h-4 w-4 self-center rounded-full" alt="reach-vb's picture" src="https://cdn-avatars.huggingface.co/v1/production/uploads/1655385361868-61b85ce86eb1f2c5e6233736.jpeg">
			<div class="mr-4 flex flex-none items-center truncate"><a class="hover:underline" href="/reach-vb">reach-vb
					</a>
				<span class="max-w-[175px] truncate border font-semibold leading-snug sm:max-w-xs rounded-sm px-1 border-yellow-100 bg-yellow-50 text-yellow-500 dark:bg-yellow-800 dark:text-yellow-400 text-xs mt-0.5 ml-1.5 uppercase" title="member of the Hugging Face team">HF staff</span>
			</div>
		<div class="mr-4 truncate font-mono text-sm text-gray-500 hover:prose-a:underline"><!-- HTML_TAG_START -->Update README.md<!-- HTML_TAG_END --></div>
		<a class="rounded-sm border bg-gray-50 px-1.5 text-sm hover:underline dark:border-gray-800 dark:bg-gray-900" href="/datasets/mozilla-foundation/common_voice_13_0/commit/34e1cfbb8f95ea840cc84c1975e4a4088d810ce5">34e1cfb</a>
		
		<time class="ml-auto hidden flex-none truncate pl-2 text-gray-500 dark:text-gray-400 lg:block" datetime="2023-03-30T09:29:31" title="Thu, 30 Mar 2023 09:29:31 GMT">almost 2 years ago</time></div></div>
			<div class="relative flex flex-wrap items-center border px-3 py-1.5 text-sm text-gray-800 dark:border-gray-800 dark:bg-gray-900 "><div class="flex items-center gap-3 text-sm font-medium"><a class="rounded-md px-1.5 capitalize bg-gray-200 dark:bg-gray-800" href="/datasets/mozilla-foundation/common_voice_13_0/blob/main/README.md">preview</a>
						<a class="rounded-md px-1.5 capitalize " href="/datasets/mozilla-foundation/common_voice_13_0/blob/main/README.md?code=true">code</a></div>
					<div class="mx-4 text-gray-200">|</div>
				<a class="my-1 mr-4 flex items-center hover:underline " href="/datasets/mozilla-foundation/common_voice_13_0/raw/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M31 16l-7 7l-1.41-1.41L28.17 16l-5.58-5.59L24 9l7 7z" fill="currentColor"></path><path d="M1 16l7-7l1.41 1.41L3.83 16l5.58 5.59L8 23l-7-7z" fill="currentColor"></path><path d="M12.419 25.484L17.639 6l1.932.518L14.35 26z" fill="currentColor"></path></svg>
							raw
						</a><div class="SVELTE_HYDRATER contents" data-target="CopyButton" data-props="{&quot;value&quot;:&quot;https://huggingface.co/datasets/mozilla-foundation/common_voice_13_0/resolve/main/README.md&quot;,&quot;style&quot;:&quot;blank&quot;,&quot;label&quot;:&quot;Copy download link&quot;,&quot;classNames&quot;:&quot;my-1 mr-4 flex items-center no-underline hover:underline&quot;}"><button class="relative my-1 mr-4 flex items-center no-underline hover:underline       " title="Copy download link" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	<span class="ml-1.5 ">Copy download link</span>
	</button></div><a class="my-1 mr-4 flex items-center hover:underline " href="/datasets/mozilla-foundation/common_voice_13_0/commits/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 4C9.383 4 4 9.383 4 16s5.383 12 12 12s12-5.383 12-12S22.617 4 16 4zm0 2c5.535 0 10 4.465 10 10s-4.465 10-10 10S6 21.535 6 16S10.465 6 16 6zm-1 2v9h7v-2h-5V8z" fill="currentColor"></path></svg>
							history
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/datasets/mozilla-foundation/common_voice_13_0/blame/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12a12 12 0 0 1-12 12z" fill="currentColor"></path><path d="M11.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path><path d="M20.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path></svg>
							blame
						</a><a class="my-1 mr-4 flex items-center hover:underline text-green-600 dark:text-gray-300" href="/datasets/mozilla-foundation/common_voice_13_0/edit/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M2 26h28v2H2z" fill="currentColor"></path><path d="M25.4 9c.8-.8.8-2 0-2.8l-3.6-3.6c-.8-.8-2-.8-2.8 0l-15 15V24h6.4l15-15zm-5-5L24 7.6l-3 3L17.4 7l3-3zM6 22v-3.6l10-10l3.6 3.6l-10 10H6z" fill="currentColor"></path></svg>
							contribute
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/datasets/mozilla-foundation/common_voice_13_0/delete/main/README.md"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M12 12h2v12h-2z" fill="currentColor"></path><path d="M18 12h2v12h-2z" fill="currentColor"></path><path d="M4 6v2h2v20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8h2V6zm4 22V8h16v20z" fill="currentColor"></path><path d="M12 2h8v2h-8z" fill="currentColor"></path></svg>
							delete
						</a>

				<div class="mr-4 flex items-center"><div class="SVELTE_HYDRATER contents" data-target="ScanStatusBadge" data-props="{&quot;classNames&quot;:&quot;mr-2&quot;,&quot;scanStatus&quot;:{&quot;status&quot;:&quot;safe&quot;,&quot;protectAiScan&quot;:{&quot;status&quot;:&quot;unscanned&quot;},&quot;avScan&quot;:{&quot;status&quot;:&quot;safe&quot;},&quot;pickleImportScan&quot;:{&quot;status&quot;:&quot;unscanned&quot;}},&quot;repo&quot;:{&quot;_id&quot;:&quot;6423ec1c6a65460799bc12ba&quot;,&quot;gitalyUid&quot;:&quot;019a42bb293c74228f450962bd2fd237369c582148cea52f47e5c4b15efbedbc&quot;,&quot;type&quot;:&quot;dataset&quot;,&quot;name&quot;:&quot;mozilla-foundation/common_voice_13_0&quot;,&quot;config&quot;:{&quot;private&quot;:false,&quot;gated&quot;:&quot;auto&quot;,&quot;discussionsDisabled&quot;:false,&quot;duplicationDisabled&quot;:false,&quot;region&quot;:&quot;us&quot;,&quot;gitaly&quot;:{&quot;storage&quot;:&quot;default&quot;,&quot;repoUid&quot;:&quot;019a42bb293c74228f450962bd2fd237369c582148cea52f47e5c4b15efbedbc&quot;,&quot;region&quot;:&quot;us&quot;},&quot;lfs&quot;:{&quot;bucket&quot;:&quot;lfs.huggingface.co&quot;,&quot;prefix&quot;:&quot;repos/01/9a/019a42bb293c74228f450962bd2fd237369c582148cea52f47e5c4b15efbedbc&quot;,&quot;usedStorage&quot;:2474013303723,&quot;usedStorageDatasetsServer&quot;:466177463664},&quot;xet&quot;:{&quot;enabled&quot;:false,&quot;bucket&quot;:&quot;xet-bridge-us&quot;,&quot;service&quot;:&quot;cas&quot;},&quot;lastDiscussion&quot;:9,&quot;datasetsServerInfo&quot;:{&quot;viewer&quot;:&quot;viewer-partial&quot;,&quot;numRows&quot;:7176573,&quot;libraries&quot;:[&quot;datasets&quot;,&quot;mlcroissant&quot;],&quot;formats&quot;:[],&quot;modalities&quot;:[&quot;audio&quot;,&quot;text&quot;]}},&quot;updatedAt&quot;:&quot;2023-03-30T11:28:17.401Z&quot;,&quot;authorId&quot;:&quot;61a8ebef7014f3674321b9a3&quot;,&quot;creatorId&quot;:&quot;61b85ce86eb1f2c5e6233736&quot;},&quot;revision&quot;:&quot;main&quot;,&quot;filePath&quot;:&quot;README.md&quot;,&quot;openByDefault&quot;:false}"><div class="sm:relative mr-2"><button class="flex h-[1.125rem] select-none items-center gap-0.5 rounded border pl-0.5 pr-0.5 text-xs leading-tight text-gray-400 hover:cursor-pointer text-gray-400 hover:border-gray-200 hover:bg-gray-50 hover:text-gray-500 dark:border-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200 "><svg class="flex-none" width="1em" height="1em" viewBox="0 0 22 28" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M15.3634 10.3639C15.8486 10.8491 15.8486 11.6357 15.3634 12.1209L10.9292 16.5551C10.6058 16.8785 10.0814 16.8785 9.7579 16.5551L7.03051 13.8277C6.54532 13.3425 6.54532 12.5558 7.03051 12.0707C7.51569 11.5855 8.30234 11.5855 8.78752 12.0707L9.7579 13.041C10.0814 13.3645 10.6058 13.3645 10.9292 13.041L13.6064 10.3639C14.0916 9.8787 14.8782 9.8787 15.3634 10.3639Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M10.6666 27.12C4.93329 25.28 0 19.2267 0 12.7867V6.52001C0 5.40001 0.693334 4.41334 1.73333 4.01334L9.73333 1.01334C10.3333 0.786673 11 0.786673 11.6 1.02667L19.6 4.02667C20.1083 4.21658 20.5465 4.55701 20.8562 5.00252C21.1659 5.44803 21.3324 5.97742 21.3333 6.52001V12.7867C21.3333 19.24 16.4 25.28 10.6666 27.12Z" fill="currentColor" fill-opacity="0.22"></path><path d="M10.0845 1.94967L10.0867 1.94881C10.4587 1.8083 10.8666 1.81036 11.2286 1.95515L11.2387 1.95919L11.2489 1.963L19.2489 4.963L19.25 4.96342C19.5677 5.08211 19.8416 5.29488 20.0351 5.57333C20.2285 5.85151 20.3326 6.18203 20.3333 6.52082C20.3333 6.52113 20.3333 6.52144 20.3333 6.52176L20.3333 12.7867C20.3333 18.6535 15.8922 24.2319 10.6666 26.0652C5.44153 24.2316 1 18.6409 1 12.7867V6.52001C1 5.82357 1.42893 5.20343 2.08883 4.94803L10.0845 1.94967Z" stroke="currentColor" stroke-opacity="0.30" stroke-width="2"></path></svg>

			<span class="mr-0.5 max-sm:hidden">Safe</span></button>

	</div></div>
						</div>

				<div class="flex items-center gap-x-3 dark:text-gray-300 sm:ml-auto">
					14.7 kB</div></div>

			<div class="relative min-h-[100px] rounded-b-lg border border-t-0 leading-tight dark:border-gray-800 dark:bg-gray-925">
				
						<div class="py-4 px-4 sm:px-6 prose hf-sanitized hf-sanitized-L7H_sqU4frO669J6USgf1"><div class="not-prose bg-linear-to-t -mx-6 -mt-4 mb-8 max-h-[300px] min-w-full overflow-auto border-b from-gray-50 px-6 pb-5 pt-4 font-mono text-xs transition-all dark:from-gray-900 dark:to-gray-950"><div class="mb-2 inline-block rounded-lg border px-2 py-1 font-mono text-xs leading-none">metadata</div>
			<pre><!-- HTML_TAG_START --><span class="hljs-attr">pretty_name:</span> <span class="hljs-string">Common</span> <span class="hljs-string">Voice</span> <span class="hljs-string">Corpus</span> <span class="hljs-number">13.0</span>
<span class="hljs-attr">annotations_creators:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">crowdsourced</span>
<span class="hljs-attr">language_creators:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">crowdsourced</span>
<span class="hljs-attr">language_bcp47:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ab</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ar</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">as</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ast</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">az</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ba</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">bas</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">be</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">bg</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">bn</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">br</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ca</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ckb</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">cnh</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">cs</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">cv</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">cy</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">da</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">de</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">dv</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">dyu</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">el</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">en</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">eo</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">es</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">et</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">eu</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">fa</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">fi</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">fr</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">fy-NL</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ga-IE</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">gl</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">gn</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ha</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">hi</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">hsb</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">hu</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">hy-AM</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ia</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">id</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ig</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">is</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">it</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ja</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ka</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">kab</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">kk</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">kmr</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ko</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ky</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">lg</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">lo</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">lt</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">lv</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">mdf</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">mhr</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">mk</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ml</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">mn</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">mr</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">mrj</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">mt</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">myv</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">nan-tw</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ne-NP</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">nl</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">nn-NO</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">oc</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">or</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">pa-IN</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">pl</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">pt</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">quy</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">rm-sursilv</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">rm-vallader</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ro</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ru</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">rw</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">sah</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">sat</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">sc</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">sk</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">skr</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">sl</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">sr</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">sv-SE</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">sw</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ta</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">th</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ti</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">tig</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">tk</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">tok</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">tr</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">tt</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">tw</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ug</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">uk</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">ur</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">uz</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">vi</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">vot</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">yo</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">yue</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">zh-CN</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">zh-HK</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">zh-TW</span>
<span class="hljs-attr">license:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">cc0-1.0</span>
<span class="hljs-attr">multilinguality:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">multilingual</span>
<span class="hljs-attr">size_categories:</span>
  <span class="hljs-attr">ab:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">ar:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">as:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">ast:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">az:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">ba:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">bas:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">be:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1M&lt;n&lt;10M</span>
  <span class="hljs-attr">bg:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">bn:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1M&lt;n&lt;10M</span>
  <span class="hljs-attr">br:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">ca:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1M&lt;n&lt;10M</span>
  <span class="hljs-attr">ckb:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">cnh:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">cs:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">cv:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">cy:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">da:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">de:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">dv:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">dyu:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">el:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">en:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1M&lt;n&lt;10M</span>
  <span class="hljs-attr">eo:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1M&lt;n&lt;10M</span>
  <span class="hljs-attr">es:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1M&lt;n&lt;10M</span>
  <span class="hljs-attr">et:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">eu:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">fa:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">fi:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">fr:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">fy-NL:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">ga-IE:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">gl:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">gn:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">ha:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">hi:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">hsb:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">hu:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">hy-AM:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">ia:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">id:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">ig:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">is:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">it:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">ja:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">ka:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">kab:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">kk:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">kmr:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">ko:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">ky:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">lg:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">lo:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">lt:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">lv:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">mdf:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">mhr:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">mk:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">ml:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">mn:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">mr:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">mrj:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">mt:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">myv:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">nan-tw:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">ne-NP:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">nl:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">nn-NO:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">oc:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">or:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">pa-IN:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">pl:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">pt:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">quy:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">rm-sursilv:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">rm-vallader:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">ro:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">ru:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">rw:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1M&lt;n&lt;10M</span>
  <span class="hljs-attr">sah:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">sat:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">sc:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">sk:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">skr:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">sl:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">sr:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">sv-SE:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">sw:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">ta:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">th:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">ti:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">tig:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">tk:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">tok:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">tr:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">tt:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">tw:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">ug:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">uk:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">ur:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">uz:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">vi:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">vot:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">n&lt;1K</span>
  <span class="hljs-attr">yo:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">1K&lt;n&lt;10K</span>
  <span class="hljs-attr">yue:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">10K&lt;n&lt;100K</span>
  <span class="hljs-attr">zh-CN:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">zh-HK:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
  <span class="hljs-attr">zh-TW:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">100K&lt;n&lt;1M</span>
<span class="hljs-attr">source_datasets:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">extended|common_voice</span>
<span class="hljs-attr">task_categories:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">automatic-speech-recognition</span>
<span class="hljs-attr">paperswithcode_id:</span> <span class="hljs-string">common-voice</span>
<span class="hljs-attr">extra_gated_prompt:</span> <span class="hljs-string">&gt;-</span>
<span class="hljs-string">  By clicking on “Access repository” below, you also agree to not attempt to</span>
<span class="hljs-string">  determine the identity of speakers in the Common Voice dataset.</span>
<span class="hljs-string"></span><!-- HTML_TAG_END --></pre></div>
	<!-- HTML_TAG_START --><h1 class="relative group flex items-center">
	<a rel="nofollow" href="#dataset-card-for-common-voice-corpus-130" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="dataset-card-for-common-voice-corpus-130">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Dataset Card for Common Voice Corpus 13.0
	</span>
</h1>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#table-of-contents" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="table-of-contents">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Table of Contents
	</span>
</h2>
<ul>
<li><a rel="nofollow" href="#dataset-description">Dataset Description</a><ul>
<li><a rel="nofollow" href="#dataset-summary">Dataset Summary</a></li>
<li><a rel="nofollow" href="#supported-tasks-and-leaderboards">Supported Tasks and Leaderboards</a></li>
<li><a rel="nofollow" href="#languages">Languages</a></li>
<li><a rel="nofollow" href="#how-to-use">How to use</a></li>
</ul>
</li>
<li><a rel="nofollow" href="#dataset-structure">Dataset Structure</a><ul>
<li><a rel="nofollow" href="#data-instances">Data Instances</a></li>
<li><a rel="nofollow" href="#data-fields">Data Fields</a></li>
<li><a rel="nofollow" href="#data-splits">Data Splits</a></li>
</ul>
</li>
<li><a rel="nofollow" href="#dataset-creation">Dataset Creation</a><ul>
<li><a rel="nofollow" href="#curation-rationale">Curation Rationale</a></li>
<li><a rel="nofollow" href="#source-data">Source Data</a></li>
<li><a rel="nofollow" href="#annotations">Annotations</a></li>
<li><a rel="nofollow" href="#personal-and-sensitive-information">Personal and Sensitive Information</a></li>
</ul>
</li>
<li><a rel="nofollow" href="#considerations-for-using-the-data">Considerations for Using the Data</a><ul>
<li><a rel="nofollow" href="#social-impact-of-dataset">Social Impact of Dataset</a></li>
<li><a rel="nofollow" href="#discussion-of-biases">Discussion of Biases</a></li>
<li><a rel="nofollow" href="#other-known-limitations">Other Known Limitations</a></li>
</ul>
</li>
<li><a rel="nofollow" href="#additional-information">Additional Information</a><ul>
<li><a rel="nofollow" href="#dataset-curators">Dataset Curators</a></li>
<li><a rel="nofollow" href="#licensing-information">Licensing Information</a></li>
<li><a rel="nofollow" href="#citation-information">Citation Information</a></li>
<li><a rel="nofollow" href="#contributions">Contributions</a></li>
</ul>
</li>
</ul>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#dataset-description" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="dataset-description">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Dataset Description
	</span>
</h2>
<ul>
<li><strong>Homepage:</strong> <a rel="nofollow" href="https://commonvoice.mozilla.org/en/datasets">https://commonvoice.mozilla.org/en/datasets</a></li>
<li><strong>Repository:</strong> <a rel="nofollow" href="https://github.com/common-voice/common-voice">https://github.com/common-voice/common-voice</a></li>
<li><strong>Paper:</strong> <a rel="nofollow" href="https://arxiv.org/abs/1912.06670">https://arxiv.org/abs/1912.06670</a></li>
<li><strong>Leaderboard:</strong> <a rel="nofollow" href="https://paperswithcode.com/dataset/common-voice">https://paperswithcode.com/dataset/common-voice</a></li>
<li><strong>Point of Contact:</strong> <a rel="nofollow" href="mailto:vaibhav@huggingface.co">Vaibhav Srivastav</a></li>
</ul>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#dataset-summary" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="dataset-summary">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Dataset Summary
	</span>
</h3>
<p>The Common Voice dataset consists of a unique MP3 and corresponding text file. 
Many of the 27141 recorded hours in the dataset also include demographic metadata like age, sex, and accent 
that can help improve the accuracy of speech recognition engines.</p>
<p>The dataset currently consists of 17689 validated hours in 108 languages, but more voices and languages are always added. 
Take a look at the <a rel="nofollow" href="https://commonvoice.mozilla.org/en/languages">Languages</a> page to request a language or start contributing.</p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#supported-tasks-and-leaderboards" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="supported-tasks-and-leaderboards">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Supported Tasks and Leaderboards
	</span>
</h3>
<p>The results for models trained on the Common Voice datasets are available via the 
<a rel="nofollow" href="https://huggingface.co/spaces/autoevaluate/leaderboards?dataset=mozilla-foundation%2Fcommon_voice_11_0&amp;only_verified=0&amp;task=automatic-speech-recognition&amp;config=ar&amp;split=test&amp;metric=wer">🤗 Autoevaluate Leaderboard</a></p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#languages" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="languages">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Languages
	</span>
</h3>
<pre><code>Abkhaz, Arabic, Armenian, Assamese, Asturian, Azerbaijani, Basaa, Bashkir, Basque, Belarusian, Bengali, Breton, Bulgarian, Cantonese, Catalan, Central Kurdish, Chinese (China), Chinese (Hong Kong), Chinese (Taiwan), Chuvash, Czech, Danish, Dhivehi, Dioula, Dutch, English, Erzya, Esperanto, Estonian, Finnish, French, Frisian, Galician, Georgian, German, Greek, Guarani, Hakha Chin, Hausa, Hill Mari, Hindi, Hungarian, Icelandic, Igbo, Indonesian, Interlingua, Irish, Italian, Japanese, Kabyle, Kazakh, Kinyarwanda, Korean, Kurmanji Kurdish, Kyrgyz, Lao, Latvian, Lithuanian, Luganda, Macedonian, Malayalam, Maltese, Marathi, Meadow Mari, Moksha, Mongolian, Nepali, Norwegian Nynorsk, Occitan, Odia, Persian, Polish, Portuguese, Punjabi, Quechua Chanka, Romanian, Romansh Sursilvan, Romansh Vallader, Russian, Sakha, Santali (Ol Chiki), Saraiki, Sardinian, Serbian, Slovak, Slovenian, Sorbian, Upper, Spanish, Swahili, Swedish, Taiwanese (Minnan), Tamil, Tatar, Thai, Tigre, Tigrinya, Toki Pona, Turkish, Turkmen, Twi, Ukrainian, Urdu, Uyghur, Uzbek, Vietnamese, Votic, Welsh, Yoruba
</code></pre>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#how-to-use" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="how-to-use">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		How to use
	</span>
</h2>
<p>The <code>datasets</code> library allows you to load and pre-process your dataset in pure Python, at scale. The dataset can be downloaded and prepared in one call to your local drive by using the <code>load_dataset</code> function. </p>
<p>For example, to download the Hindi config, simply specify the corresponding language config name (i.e., "hi" for Hindi):</p>
<pre><code class="language-python"><span class="hljs-keyword">from</span> datasets <span class="hljs-keyword">import</span> load_dataset

cv_13 = load_dataset(<span class="hljs-string">"mozilla-foundation/common_voice_13_0"</span>, <span class="hljs-string">"hi"</span>, split=<span class="hljs-string">"train"</span>)
</code></pre>
<p>Using the datasets library, you can also stream the dataset on-the-fly by adding a <code>streaming=True</code> argument to the <code>load_dataset</code> function call. Loading a dataset in streaming mode loads individual samples of the dataset at a time, rather than downloading the entire dataset to disk.</p>
<pre><code class="language-python"><span class="hljs-keyword">from</span> datasets <span class="hljs-keyword">import</span> load_dataset

cv_13 = load_dataset(<span class="hljs-string">"mozilla-foundation/common_voice_13_0"</span>, <span class="hljs-string">"hi"</span>, split=<span class="hljs-string">"train"</span>, streaming=<span class="hljs-literal">True</span>)

<span class="hljs-built_in">print</span>(<span class="hljs-built_in">next</span>(<span class="hljs-built_in">iter</span>(cv_13)))
</code></pre>
<p><em>Bonus</em>: create a <a rel="nofollow" href="https://huggingface.co/docs/datasets/use_with_pytorch">PyTorch dataloader</a> directly with your own datasets (local/streamed).</p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#local" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="local">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Local
	</span>
</h3>
<pre><code class="language-python"><span class="hljs-keyword">from</span> datasets <span class="hljs-keyword">import</span> load_dataset
<span class="hljs-keyword">from</span> torch.utils.data.sampler <span class="hljs-keyword">import</span> BatchSampler, RandomSampler

cv_13 = load_dataset(<span class="hljs-string">"mozilla-foundation/common_voice_13_0"</span>, <span class="hljs-string">"hi"</span>, split=<span class="hljs-string">"train"</span>)
batch_sampler = BatchSampler(RandomSampler(cv_13), batch_size=<span class="hljs-number">32</span>, drop_last=<span class="hljs-literal">False</span>)
dataloader = DataLoader(cv_13, batch_sampler=batch_sampler)
</code></pre>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#streaming" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="streaming">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Streaming
	</span>
</h3>
<pre><code class="language-python"><span class="hljs-keyword">from</span> datasets <span class="hljs-keyword">import</span> load_dataset
<span class="hljs-keyword">from</span> torch.utils.data <span class="hljs-keyword">import</span> DataLoader

cv_13 = load_dataset(<span class="hljs-string">"mozilla-foundation/common_voice_13_0"</span>, <span class="hljs-string">"hi"</span>, split=<span class="hljs-string">"train"</span>)
dataloader = DataLoader(cv_13, batch_size=<span class="hljs-number">32</span>)
</code></pre>
<p>To find out more about loading and preparing audio datasets, head over to <a rel="nofollow" href="https://huggingface.co/blog/audio-datasets">hf.co/blog/audio-datasets</a>.</p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#example-scripts" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="example-scripts">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Example scripts
	</span>
</h3>
<p>Train your own CTC or Seq2Seq Automatic Speech Recognition models on Common Voice 13 with <code>transformers</code> - <a rel="nofollow" href="https://github.com/huggingface/transformers/tree/main/examples/pytorch/speech-recognition">here</a>.</p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#dataset-structure" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="dataset-structure">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Dataset Structure
	</span>
</h2>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#data-instances" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="data-instances">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Data Instances
	</span>
</h3>
<p>A typical data point comprises the <code>path</code> to the audio file and its <code>sentence</code>. 
Additional fields include <code>accent</code>, <code>age</code>, <code>client_id</code>, <code>up_votes</code>, <code>down_votes</code>, <code>gender</code>, <code>locale</code> and <code>segment</code>.</p>
<pre><code class="language-python">{
  <span class="hljs-string">'client_id'</span>: <span class="hljs-string">'d59478fbc1ee646a28a3c652a119379939123784d99131b865a89f8b21c81f69276c48bd574b81267d9d1a77b83b43e6d475a6cfc79c232ddbca946ae9c7afc5'</span>, 
  <span class="hljs-string">'path'</span>: <span class="hljs-string">'et/clips/common_voice_et_18318995.mp3'</span>, 
  <span class="hljs-string">'audio'</span>: {
    <span class="hljs-string">'path'</span>: <span class="hljs-string">'et/clips/common_voice_et_18318995.mp3'</span>, 
    <span class="hljs-string">'array'</span>: array([-<span class="hljs-number">0.00048828</span>, -<span class="hljs-number">0.00018311</span>, -<span class="hljs-number">0.00137329</span>, ...,  <span class="hljs-number">0.00079346</span>, <span class="hljs-number">0.00091553</span>,  <span class="hljs-number">0.00085449</span>], dtype=float32), 
    <span class="hljs-string">'sampling_rate'</span>: <span class="hljs-number">48000</span>
  }, 
  <span class="hljs-string">'sentence'</span>: <span class="hljs-string">'Tasub kokku saada inimestega, keda tunned juba ammust ajast saati.'</span>, 
  <span class="hljs-string">'up_votes'</span>: <span class="hljs-number">2</span>, 
  <span class="hljs-string">'down_votes'</span>: <span class="hljs-number">0</span>, 
  <span class="hljs-string">'age'</span>: <span class="hljs-string">'twenties'</span>, 
  <span class="hljs-string">'gender'</span>: <span class="hljs-string">'male'</span>, 
  <span class="hljs-string">'accent'</span>: <span class="hljs-string">''</span>, 
  <span class="hljs-string">'locale'</span>: <span class="hljs-string">'et'</span>, 
  <span class="hljs-string">'segment'</span>: <span class="hljs-string">''</span>
}
</code></pre>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#data-fields" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="data-fields">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Data Fields
	</span>
</h3>
<p><code>client_id</code> (<code>string</code>): An id for which client (voice) made the recording</p>
<p><code>path</code> (<code>string</code>): The path to the audio file</p>
<p><code>audio</code> (<code>dict</code>): A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate. Note that when accessing the audio column: <code>dataset[0]["audio"]</code> the audio file is automatically decoded and resampled to <code>dataset.features["audio"].sampling_rate</code>. Decoding and resampling of a large number of audio files might take a significant amount of time. Thus it is important to first query the sample index before the <code>"audio"</code> column, <em>i.e.</em> <code>dataset[0]["audio"]</code> should <strong>always</strong> be preferred over <code>dataset["audio"][0]</code>.</p>
<p><code>sentence</code> (<code>string</code>): The sentence the user was prompted to speak</p>
<p><code>up_votes</code> (<code>int64</code>): How many upvotes the audio file has received from reviewers</p>
<p><code>down_votes</code> (<code>int64</code>): How many downvotes the audio file has received from reviewers</p>
<p><code>age</code> (<code>string</code>): The age of the speaker (e.g. <code>teens</code>, <code>twenties</code>, <code>fifties</code>)</p>
<p><code>gender</code> (<code>string</code>): The gender of the speaker</p>
<p><code>accent</code> (<code>string</code>): Accent of the speaker</p>
<p><code>locale</code> (<code>string</code>): The locale of the speaker</p>
<p><code>segment</code> (<code>string</code>): Usually an empty field</p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#data-splits" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="data-splits">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Data Splits
	</span>
</h3>
<p>The speech material has been subdivided into portions for dev, train, test, validated, invalidated, reported and other.</p>
<p>The validated data is data that has been validated with reviewers and received upvotes that the data is of high quality.</p>
<p>The invalidated data is data has been invalidated by reviewers
and received downvotes indicating that the data is of low quality.</p>
<p>The reported data is data that has been reported, for different reasons.</p>
<p>The other data is data that has not yet been reviewed.</p>
<p>The dev, test, train are all data that has been reviewed, deemed of high quality and split into dev, test and train.</p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#data-preprocessing-recommended-by-hugging-face" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="data-preprocessing-recommended-by-hugging-face">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Data Preprocessing Recommended by Hugging Face
	</span>
</h2>
<p>The following are data preprocessing steps advised by the Hugging Face team. They are accompanied by an example code snippet that shows how to put them to practice. </p>
<p>Many examples in this dataset have trailing quotations marks, e.g <em>“the cat sat on the mat.“</em>. These trailing quotation marks do not change the actual meaning of the sentence, and it is near impossible to infer whether a sentence is a quotation or not a quotation from audio data alone. In these cases, it is advised to strip the quotation marks, leaving: <em>the cat sat on the mat</em>.</p>
<p>In addition, the majority of training sentences end in punctuation ( . or ? or ! ), whereas just a small proportion do not. In the dev set, <strong>almost all</strong> sentences end in punctuation. Thus, it is recommended to append a full-stop ( . ) to the end of the small number of training examples that do not end in punctuation.</p>
<pre><code class="language-python"><span class="hljs-keyword">from</span> datasets <span class="hljs-keyword">import</span> load_dataset

ds = load_dataset(<span class="hljs-string">"mozilla-foundation/common_voice_13_0"</span>, <span class="hljs-string">"en"</span>, use_auth_token=<span class="hljs-literal">True</span>)

<span class="hljs-keyword">def</span> <span class="hljs-title function_">prepare_dataset</span>(<span class="hljs-params">batch</span>):
  <span class="hljs-string">"""Function to preprocess the dataset with the .map method"""</span>
  transcription = batch[<span class="hljs-string">"sentence"</span>]
  
  <span class="hljs-keyword">if</span> transcription.startswith(<span class="hljs-string">'"'</span>) <span class="hljs-keyword">and</span> transcription.endswith(<span class="hljs-string">'"'</span>):
    <span class="hljs-comment"># we can remove trailing quotation marks as they do not affect the transcription</span>
    transcription = transcription[<span class="hljs-number">1</span>:-<span class="hljs-number">1</span>]
  
  <span class="hljs-keyword">if</span> transcription[-<span class="hljs-number">1</span>] <span class="hljs-keyword">not</span> <span class="hljs-keyword">in</span> [<span class="hljs-string">"."</span>, <span class="hljs-string">"?"</span>, <span class="hljs-string">"!"</span>]:
    <span class="hljs-comment"># append a full-stop to sentences that do not end in punctuation</span>
    transcription = transcription + <span class="hljs-string">"."</span>
  
  batch[<span class="hljs-string">"sentence"</span>] = transcription
  
  <span class="hljs-keyword">return</span> batch

ds = ds.<span class="hljs-built_in">map</span>(prepare_dataset, desc=<span class="hljs-string">"preprocess dataset"</span>)
</code></pre>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#dataset-creation" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="dataset-creation">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Dataset Creation
	</span>
</h2>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#curation-rationale" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="curation-rationale">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Curation Rationale
	</span>
</h3>
<p>[Needs More Information]</p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#source-data" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="source-data">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Source Data
	</span>
</h3>
<h4 class="relative group flex items-center">
	<a rel="nofollow" href="#initial-data-collection-and-normalization" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="initial-data-collection-and-normalization">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Initial Data Collection and Normalization
	</span>
</h4>
<p>[Needs More Information]</p>
<h4 class="relative group flex items-center">
	<a rel="nofollow" href="#who-are-the-source-language-producers" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="who-are-the-source-language-producers">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Who are the source language producers?
	</span>
</h4>
<p>[Needs More Information]</p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#annotations" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="annotations">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Annotations
	</span>
</h3>
<h4 class="relative group flex items-center">
	<a rel="nofollow" href="#annotation-process" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="annotation-process">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Annotation process
	</span>
</h4>
<p>[Needs More Information]</p>
<h4 class="relative group flex items-center">
	<a rel="nofollow" href="#who-are-the-annotators" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="who-are-the-annotators">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Who are the annotators?
	</span>
</h4>
<p>[Needs More Information]</p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#personal-and-sensitive-information" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="personal-and-sensitive-information">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Personal and Sensitive Information
	</span>
</h3>
<p>The dataset consists of people who have donated their voice online.  You agree to not attempt to determine the identity of speakers in the Common Voice dataset.</p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#considerations-for-using-the-data" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="considerations-for-using-the-data">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Considerations for Using the Data
	</span>
</h2>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#social-impact-of-dataset" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="social-impact-of-dataset">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Social Impact of Dataset
	</span>
</h3>
<p>The dataset consists of people who have donated their voice online.  You agree to not attempt to determine the identity of speakers in the Common Voice dataset.</p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#discussion-of-biases" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="discussion-of-biases">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Discussion of Biases
	</span>
</h3>
<p>[More Information Needed] </p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#other-known-limitations" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="other-known-limitations">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Other Known Limitations
	</span>
</h3>
<p>[More Information Needed] </p>
<h2 class="relative group flex items-center">
	<a rel="nofollow" href="#additional-information" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="additional-information">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Additional Information
	</span>
</h2>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#dataset-curators" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="dataset-curators">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Dataset Curators
	</span>
</h3>
<p>[More Information Needed] </p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#licensing-information" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="licensing-information">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Licensing Information
	</span>
</h3>
<p>Public Domain, <a rel="nofollow" href="https://creativecommons.org/share-your-work/public-domain/cc0/">CC-0</a></p>
<h3 class="relative group flex items-center">
	<a rel="nofollow" href="#citation-information" class="block pr-1.5 text-lg md:absolute md:p-1.5 md:opacity-0 md:group-hover:opacity-100 md:right-full" id="citation-information">
		<span class="header-link"><svg viewBox="0 0 256 256" preserveAspectRatio="xMidYMid meet" height="1em" width="1em" role="img" aria-hidden="true" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" class="text-gray-500 hover:text-black dark:hover:text-gray-200 w-4"><path fill="currentColor" d="M167.594 88.393a8.001 8.001 0 0 1 0 11.314l-67.882 67.882a8 8 0 1 1-11.314-11.315l67.882-67.881a8.003 8.003 0 0 1 11.314 0zm-28.287 84.86l-28.284 28.284a40 40 0 0 1-56.567-56.567l28.284-28.284a8 8 0 0 0-11.315-11.315l-28.284 28.284a56 56 0 0 0 79.196 79.197l28.285-28.285a8 8 0 1 0-11.315-11.314zM212.852 43.14a56.002 56.002 0 0 0-79.196 0l-28.284 28.284a8 8 0 1 0 11.314 11.314l28.284-28.284a40 40 0 0 1 56.568 56.567l-28.285 28.285a8 8 0 0 0 11.315 11.314l28.284-28.284a56.065 56.065 0 0 0 0-79.196z"></path></svg></span>
	</a>
	<span>
		Citation Information
	</span>
</h3>
<pre><code>@inproceedings{commonvoice:2020,
  author = {Ardila, R. and Branson, M. and Davis, K. and Henretty, M. and Kohler, M. and Meyer, J. and Morais, R. and Saunders, L. and Tyers, F. M. and Weber, G.},
  title = {Common Voice: A Massively-Multilingual Speech Corpus},
  booktitle = {Proceedings of the 12th Conference on Language Resources and Evaluation (LREC 2020)},
  pages = {4211--4215},
  year = 2020
}
</code></pre>
<!-- HTML_TAG_END --></div>
</div></section></div></main>

	</div>

		<script>
			import("\/front\/build\/kube-a9fae47\/index.js");
			window.moonSha = "kube-a9fae47\/";
			window.__hf_deferred = {};
		</script>

		<!-- Stripe -->
		<script>
			if (["hf.co", "huggingface.co"].includes(window.location.hostname)) {
				const script = document.createElement("script");
				script.src = "https://js.stripe.com/v3/";
				script.async = true;
				document.head.appendChild(script);
			}
		</script>
	</body>
</html>
