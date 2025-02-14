<!-- src/lib/layouts/Auth.svelte -->
<script>
	import { auth } from '$lib/store';
</script>

{#if $auth.user}
	<slot />
{:else}
	<p>Bạn cần đăng nhập để truy cập nội dung này.</p>
{/if}
