<!-- src/lib/components/Button.svelte -->
<script lang="ts">
	export let type: 'button' | 'submit' | 'reset' = 'button';
	export let disabled = false;
</script>

<button
	{type}
	{disabled}
	class="rounded bg-blue-500 px-4 py-2 text-white hover:bg-blue-700 disabled:bg-gray-400"
>
	<slot />
</button>
