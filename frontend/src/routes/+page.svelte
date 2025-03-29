<script>
    import { goto } from '$app/navigation';
    import { user } from '../stores/auth';
    import { Pane, Splitpanes } from 'svelte-splitpanes';
    import { onMount } from 'svelte';
    
    onMount(() => {
    });

</script>
  
<main class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">Chat</h1>
    <p class="text-gray-500">Sup dawgzzzz</p>
    <Splitpanes class="default-theme" style="height: 400px">
      <Pane minSize={20}>This is where the chatbot will go</Pane>
      <Pane>This is where environmental info will go</Pane>
    </Splitpanes>
  </main>
  