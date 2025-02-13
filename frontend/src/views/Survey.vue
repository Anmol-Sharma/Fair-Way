<script setup>
import { ref } from "vue";

sessionStorage.clear();

let survey = ref({
  easeOfUse: "",
  sliderVal: "",
  recommendation: "",
  fairFamiliarity: "",
  priorUsage: "",
  usefulness: "",
  usefulAspects: [],
  futureUsage: "",
  comments: "",
});

async function handleSubmit(event) {
  // Handle form submission here
  //   console.log("Survey submitted:", this.survey);
  // You can add your submission logic here
}
</script>

<template>
  <div
    class="container-fluid main-container d-flex justify-content-center align-content-center my-3"
  >
    <div class="card">
      <div class="card-body">
        <h1 class="card-title">FAIR-Way Survey</h1>
        <p class="card-text my-4">
          Your valuable feedback helps us improve this tool even further.
        </p>
        <form @submit.prevent="handleSubmit">
          <!-- Section 1: General Feedback -->
          <h2 class="text-center">General Feedback</h2>
          <div class="row my-3">
            <label class="form-label"
              >How would you rate the overall ease of use of the tool?</label
            >
            <select class="form-select" v-model="survey.easeOfUse">
              <option value="">Please select</option>
              <option>Very Easy</option>
              <option>Easy</option>
              <option>Neutral</option>
              <option>Difficult</option>
              <option>Very Difficult</option>
            </select>
          </div>

          <div class="row my-3">
            <label class="form-label">Would you recommend this tool to others?</label>
            <select class="form-select" v-model="survey.recommendation">
              <option value="">Please select</option>
              <option>Definitely Yes</option>
              <option>Yes</option>
              <option>Neutral</option>
              <option>No</option>
              <option>Definitely No</option>
            </select>
          </div>

          <!-- Section 2: Prior Experience -->
          <h2 class="text-center">Prior Experience</h2>
          <div class="row my-3">
            <label class="form-label">How familiar are you with FAIR data principles?</label>
            <select class="form-select" v-model="survey.fairFamiliarity">
              <option value="">Please select</option>
              <option>Very Familiar</option>
              <option>Familiar</option>
              <option>Neutral</option>
              <option>Unfamiliar</option>
              <option>Very Unfamiliar</option>
            </select>
          </div>

          <div class="row my-3">
            <label class="form-label">Have you used other FAIR assessment tools before?</label>
            <select class="form-select" v-model="survey.priorUsage">
              <option value="">Please select</option>
              <option>Yes, frequently</option>
              <option>Yes, occasionally</option>
              <option>No</option>
            </select>
          </div>

          <div class="row my-3">
            <label class="form-label">What is your Background?</label>
            <select class="form-select" v-model="survey.fairFamiliarity">
              <option value="">Please select</option>
              <option>Computer Sciences/ IT</option>
              <option>Natural Sciences</option>
              <option>Medical Sciences</option>
              <option>Earth & Environmental Sciences</option>
              <option>Agricultural Sciences</option>
              <option>Other</option>
            </select>
          </div>

          <!-- Section 3: Tool Usefulness -->
          <h2 class="text-center">Tool Usefulness</h2>
          <div class="row my-3">
            <label class="form-label"
              >How useful did you find the tool for FAIR assessment of your datasets?</label
            >
            <select class="form-select" v-model="survey.usefulness">
              <option value="">Please select</option>
              <option>Extremely Useful</option>
              <option>Very Useful</option>
              <option>Neutral</option>
              <option>Slightly Useful</option>
              <option>Not Useful</option>
            </select>
          </div>

          <div class="row my-4">
            <label class="form-label"
              >How effective do you think the tool is in assessing FAIR data? Please Rate out of
              10</label
            >
            <div class="slider-container">
              <!-- Bubble -->
              <span
                class="badge rounded-pill bg-primary bubble position-absolute"
                :style="{ left: ((survey.sliderVal - 0) * 100) / 10 + '%' }"
              >
                {{ survey.sliderVal }}
              </span>

              <!-- Slider -->
              <div class="input-group">
                <input
                  type="range"
                  class="form-range"
                  min="0"
                  max="10"
                  step="1"
                  v-model="survey.sliderVal"
                />
              </div>
            </div>
          </div>

          <div class="row my-3">
            <label class="form-label"
              >Which type of Assessment(s) have you tried with the Tool?</label
            >
            <select class="form-select" v-model="survey.usefulAspects">
              <option value="">Please select</option>
              <option>Online</option>
              <option>Offline</option>
              <option>Both</option>
            </select>
          </div>

          <div class="row my-3">
            <label class="form-label">How likely are you to use this tool in the future?</label>
            <select class="form-select" v-model="survey.futureUsage">
              <option value="">Please select</option>
              <option>Very Likely</option>
              <option>Likely</option>
              <option>Neutral</option>
              <option>Unlikely</option>
              <option>Very Unlikely</option>
            </select>
          </div>

          <!-- Additional Comments -->
          <h2 class="text-center">Additional Comments</h2>
          <div class="row my-3 justify-content-center">
            <textarea
              class="form-control"
              rows="5"
              placeholder="Please provide any additional comments or suggestions..."
              v-model="survey.comments"
            ></textarea>
          </div>

          <!-- Submit Button -->
          <div class="text-center">
            <button type="submit" class="btn btn-primary">Submit Survey</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-container {
  background-color: #ffffff;
  max-width: 85vw;
}

.main-container h1 {
  font-size: 3em; /* Default size, can be overridden */
}

.form-control {
  width: 80%;
}

.card-title {
  font-size: 2.5rem;
}

.card-text {
  font-size: 1.2rem;
  margin: 5px;
}

.btn {
  position: relative;
}

.card-body {
  min-width: 70rem;
  min-height: 30rem;
}

.slider-container {
  position: relative;
  width: 80%;
  padding-top: 2rem; /* Space for the bubble */
  padding-bottom: 1rem; /* Space for the bubble */
}

.bubble {
  transform: translateX(-50%);
  top: 0;
  font-size: 0.875rem;
  padding: 0.25rem 0.75rem;
  transition: left 0.2s ease-in-out;
}

.form-range {
  width: 100%;
}
</style>
