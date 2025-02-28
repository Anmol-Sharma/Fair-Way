<script setup>
import { ref } from "vue";

const props = defineProps({
  showOnlineFlag: {
    type: Boolean,
    default: true,
  },
});

// Bind the url in input form to this variable
let resourceUrl = ref();

const emit = defineEmits(["formSubmit"]);

const handleSubmit = () => {
  const doiPattern = /^(?:https?:\/\/)?doi\.org\/10\.\d+\/(?:dryad|zenodo)(?:\.[\w-]+)*$/;
  const zenodoPattern = /^(https?:\/\/)?zenodo\.org\/records\/\d+$/;
  const dryadPattern =
    /^(https?:\/\/)datadryad\.org\/stash\/dataset\/doi:10\.\d+\/dryad\.[a-zA-Z0-9-]+$/;

  const huggingFacePattern =
    /^(https?:\/\/)huggingface\.co\/(?:api\/)?datasets\/[\w-]+(?:\/[\w-]+)*$/;

  if (
    !doiPattern.test(resourceUrl.value) &&
    !zenodoPattern.test(resourceUrl.value) &&
    !dryadPattern.test(resourceUrl.value) &&
    !huggingFacePattern.test(resourceUrl.value)
  ) {
    alert(
      "Invalid Record.\nOnly valid DOIs published by Zenodo or Dryad accepted or Enter valid url of a Zenodo or Dryad Record.\nOr Enter a url of a hugging face dataset."
    );
    return;
  } else {
    // Sendback the url to the parent
    emit("formSubmit", resourceUrl.value);
    resourceUrl.value = "";
  }
};
</script>

<template>
  <div class="card assess-card">
    <div class="card-body text-center">
      <h5 class="card-title">Online / Published Dataset</h5>
      <p>Enter Valid DOI of dataset from defined Data Repositories above.</p>
      <!-- TODO: Add support for hugging face datasets -->
      <form @submit.prevent="handleSubmit">
        <div class="my-4 d-flex justify-content-center">
          <div class="input-group w-75">
            <input
              type="text"
              class="form-control"
              aria-describedby="basic-addon3 basic-addon4"
              placeholder="DOI of the dataset"
              style="text-align: center"
              id="dataset_url"
              required
              v-model="resourceUrl"
            />
          </div>
        </div>
        <div class="text-center">
          <button type="submit" class="btn btn-primary">Start Assessment</button>
        </div>
        <!-- Add help section with examples -->
        <div class="mt-4 text-center" v-if="props.showOnlineFlag">
          <p class="text-muted small-text-2">Not sure what to test? Try the example below:</p>
          <div class="mt-1">
            <a
              href="https://doi.org/10.5061/dryad.ngf1vhj3t"
              target="_blank"
              class="text-decoration-none text-muted small-text-2"
            >
              Example (Dryad Dataset) : https://doi.org/10.5061/dryad.ngf1vhj3t
            </a>
            <br />
            Copy and Paste this link above & click "Start Assessment"
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.card {
  min-height: 27em;
  max-width: 45vw;
}

p {
  font-size: 1.2em;
}
</style>
