<script setup>
const props = defineProps({
  // Accordion object with title, body and id
  acc: {
    type: Object,
    required: true,
  },
});

const acc_head_id = props.acc.id + "_head";
const accordion_name_parent = "#" + props.acc.id;
const collapse_id = "collapse_" + props.acc.id;
const collapse_id_target = "#" + collapse_id;
</script>

<template>
  <div class="accordion my-3 px-4" :id="acc.id">
    <div class="accordion-item text">
      <h2 class="accordion-header" :id="acc_head_id">
        <button
          class="accordion-button fw-bold"
          type="button"
          data-bs-toggle="collapse"
          :data-bs-target="collapse_id_target"
          aria-expanded="false"
          :aria-controls="collapse_id"
          :style="{ backgroundColor: acc.color }"
        >
          {{ acc.title }}
        </button>
      </h2>
      <div
        :id="collapse_id"
        class="accordion-collapse collapse"
        :aria-labelledby="acc_head_id"
        :data-bs-parent="accordion_name_parent"
      >
        <div class="accordion-body border rounded-3 border-1">
          <div class="row mb-2">
            <div class="col-md-2"><b>Score:</b></div>
            <div class="col-md-10">
              {{ acc.metric_analysis.score }} out of {{ acc.metric_analysis.out_of }}
            </div>
          </div>
          <div class="col-md-2"><b>Test Results:</b></div>
          <br />
          <div v-for="(value, test) in acc.metric_analysis.test_results">
            <div class="row mb-3">
              <div class="col-2">
                <i>{{ test }}</i>
              </div>
              <div class="col-10">
                <pre class="text-muted"><code>{{ value }}</code></pre>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.accordion {
  min-width: 80vw;
  max-width: 85vw;
}

.accordion-button {
  font-size: 0.55em;
}

.accordion-button:focus {
  outline: none; /* Remove the default focus outline */
  box-shadow: 0 0 0 3px #121111;
}
</style>
