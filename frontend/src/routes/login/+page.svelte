<!-- src/routes/Login.svelte -->
<script>
	import { handleLogin, auth } from '$lib/store';

	let username = '';
	let password = '';

	async function loginUser() {
		await handleLogin(username, password);
	}
</script>

<div class="mx-auto max-w-sm p-4">
	<h2 class="mb-4 text-2xl font-bold">Đăng nhập</h2>
	<input
		bind:value={username}
		type="text"
		placeholder="Username"
		class="mb-2 w-full rounded border p-2"
	/>
	<input
		bind:value={password}
		type="password"
		placeholder="Password"
		class="mb-2 w-full rounded border p-2"
	/>
	<button on:click={loginUser} class="w-full rounded bg-blue-500 p-2 text-white">Đăng nhập</button>
</div>
