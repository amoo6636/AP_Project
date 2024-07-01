<template>
    <div class="page-dashbort">

        <router-link :to="{name: 'AddProduct' }" class="button is-light mt-4">Add Product</router-link>
    
    
    <div>
        <canvas id="myChart"></canvas>
    </div>
    
    
    </div>


</template>


<script>
  const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
</script>


