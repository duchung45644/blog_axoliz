<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { requireAuth } from '$lib/auth';
	import { apiRequest } from '$lib/api';

	interface Post {
		title: string;
		content: string;
	}

	let post: Post | undefined;
	let id = $page.params.slug;

	onMount(async () => {
		requireAuth(); // Kiểm tra đăng nhập

		try {
			post = await apiRequest('get', `/posts/${id}`);
		} catch (error) {
			console.error('Lỗi tải bài viết:', error);
		}
	});
</script>

{#if post}
	<h1>{post.title}</h1>
	<p>{post.content}</p>
{:else}
	<p>Đang tải bài viết...</p>
{/if}
