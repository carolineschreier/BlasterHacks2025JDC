<script>
  import { goto } from '$app/navigation';
  import { user } from '../stores/auth';
  import { Pane, Splitpanes } from 'svelte-splitpanes';
  import { onMount } from 'svelte';
  import { Input, Label, Helper, Button, P} from 'flowbite-svelte';

  onMount(() => {
  });

  let responseVal = "";
  let chatVal = [];
  let totalEmissions = 0.0;
  let totalEmissions2 = 0.0;

  function handleClick(){
    chatVal = [...chatVal, responseVal];
    addResponse(responseVal);
    responseVal = "";

  }

  
  function addResponse(response_message) {
      fetch('http://localhost:8000/chat/', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({
              message: response_message
          })
      })
      .then((response) => response.json())
      .then((data) => {
          chatVal = [...chatVal, data["chat_response"]];
          totalEmissions = totalEmissions + data["emissions"];
          totalEmissions2 = totalEmissions2 + 4.32;
      });
  }

  function getMercuryHeight() {
      if (totalEmissions <= 0) {
          return 1;
      } else if (totalEmissions >= 0.00005 && totalEmissions < 0.00008) {
          return 2;
      } else if (totalEmissions >= 0.00008 && totalEmissions < 0.00010) {
          return 3;
      } else if (totalEmissions >= 0.00010 && totalEmissions < 0.00015) {
          return 4;
      } else if (totalEmissions >= 0.00015) {
          return 5;
      } 
      else {
          return totalEmissions;
      }
  }

  function getMercuryHeight2() {
    return ((totalEmissions2 / (4.32)) * 5) + 1;
  }
</script>

<main class="container mx-auto p-4">
  <h1 class="text-3xl font-bold mb-4">Chat</h1>
  <p class="text-gray-500">Sup dawgzzzz</p>
  <Splitpanes class="default-theme" style="height: 400px">
      <Pane minSize={100}>
          <Splitpanes class="default-theme" horizontal="{true}">
              <Pane minSize={70} class="pane" >
                  <div style= "max-height:250px; overflow-y:auto ">
                      {#each chatVal as chat, index}
                          <div style="padding-left:20px; padding-right:20px;" >
                              {#if index % 2 == 0}
                                  <P align="right" color="text-blue-700 dark:text-blue-500" size="xl">{chat}</P>
                              {:else}
                                  <P align="left" size="xl">{chat}</P>
                              {/if}
                          </div>
                      {/each} 
                  </div>       
              </Pane>
              <Pane >
                  <div class="mb-6" style="padding-left:20px; padding-right:20px; padding-top:20px" >
                      <Label for="Query" class="mb-2">Talk to the chat bot</Label>
                      <Input type="text" id="response" placeholder="Type here..." bind:value={responseVal} >
                          <Button type="submit" on:click={() => handleClick()} slot="right">Send</Button>
                      </Input>
                  </div>
              </Pane>
          </Splitpanes >
      </Pane >
      <Pane minSize={100} >
          <div>
              <P align="center" size="4xl" weight="extrabold" >Carbon Dioxide Emissions:</P>
              <div style="display: inline; float: left; padding-left:20px"> 
                <P size="4xl" weight="extrabold"> {totalEmissions} </P>
              </div>
              <div style="display: inline; float: right; padding-right:20px"> 
                <P size="4xl" weight="extrabold"> {totalEmissions2} </P>
              </div>
          </div>
          <div class="flex justify-center" style="padding-left:20px; padding-right:20px;">
              <div class="thermo" style="height: 50vh; width: 6vw; margin-right: 20px;">
                  <div class="mercury" style={`height: ${getMercuryHeight()}vh`}></div>
              </div>
              <div class="thermo" style="height: 50vh; width: 6vw;">
                  <div class="mercury" style={`height: ${getMercuryHeight2()}vh`}></div>
              </div>
          </div>

      </Pane>
  </Splitpanes>
</main>

<style>
  .pane {
      height: 200px; /* Set a fixed height */
      overflow-y: auto; /* Add vertical scrolling */
  }
  body{
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
  }
  .thermo{
      border-radius: 55px;
      background: #fff;
      box-shadow: inset 16px 16px 32px #e6e6e6, 
                  inset -16px -16px 32px #ffff;
      position: relative;
      overflow: hidden;
  }

  .mercury{
      position: absolute;
      bottom: 0;
      left: 0;
      border-radius: 55px;
      background: linear-gradient(to top, #fb7740, red);
      width: 100%;
  }
</style>