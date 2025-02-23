<script setup>
import router from "../router";
import { ref } from "vue";

let survey = ref({
  easeOfUse: "",
  recommendation: "",
  fairFamiliarity: "",
  priorUsage: "",
  priorTools: "",
  professionalStatus: "",
  academicBG: "",
  academicBgOther: "",
  usefulness: "",
  fairRating: 5,
  usefulAspects: "",
  futureUsage: "",
  comments: "",
});

// Track form validation state and touched fields
const formSubmitted = ref(false);
const touchedFields = ref(new Set());

function markFieldAsTouched(fieldName) {
  touchedFields.value.add(fieldName);
}

function isFieldRequired(fieldName) {
  return (
    fieldName !== "comments" &&
    (fieldName !== "priorTools" || survey.value.priorUsage.includes("Yes")) &&
    (fieldName !== "academicBgOther" || survey.value.academicBG.includes("Other"))
  );
}

function isFieldValid(fieldName) {
  if (!formSubmitted.value && !touchedFields.value.has(fieldName)) return true;
  if (!isFieldRequired(fieldName)) return true;
  return survey.value[fieldName] !== "";
}

function shouldShowError(fieldName) {
  return (
    isFieldRequired(fieldName) &&
    (formSubmitted.value || touchedFields.value.has(fieldName)) &&
    survey.value[fieldName] === ""
  );
}

async function handleSubmit(event) {
  formSubmitted.value = true;

  // Check if all required fields are filled
  const requiredFields = Object.keys(survey.value).filter((field) => isFieldRequired(field));
  const isValid = requiredFields.every((field) => survey.value[field] !== "");

  if (!isValid) {
    alert("Please fill in all required fields");
    return;
  }

  try {
    const req = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(survey.value),
    };

    const response = await fetch("/api/Survey", req);

    if (response.status === 500) {
      router.push({ name: "500" });
      throw new Error("Internal Server Error");
    }

    if (response.status !== 201) {
      alert("Error while processing your feedback. We'll look into it.");
      throw new Error(`HTTP response code ${response.status}. Data has not been accepted.`);
    }
    alert("Thanks for your participation in this Survey");
    // Clear form fields after submission
    survey.value = {
      easeOfUse: "",
      recommendation: "",
      fairFamiliarity: "",
      priorUsage: "",
      priorTools: "",
      professionalStatus: "",
      academicBG: "",
      academicBgOther: "",
      usefulness: "",
      fairRating: 5,
      usefulAspects: "",
      futureUsage: "",
      comments: "",
    };
    formSubmitted.value = false;
    touchedFields.value.clear();
  } catch (error) {
    console.error("Error submitting survey:", error);
    alert("Failed to submit survey. Please try again later.");
  }
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
          Your valuable feedback helps us improve this tool even further.<br />
        </p>
        <p class="text-muted fs-6">
          Before Taking this Survey, we recommend that you please try out this tool. <br />
          You can evaluate an already published data source or your local dataset metadata file.
          <br />
          For more information please read details in the
          <RouterLink class="link-primary" to="/About">About</RouterLink> section.
        </p>
        <form @submit.prevent="handleSubmit" novalidate>
          <!-- Section 1: General Feedback -->
          <h2 class="text-center">General Feedback</h2>
          <div class="row my-3">
            <label class="form-label" for="ease-of-use">
              How would you rate the overall ease of use of the tool?
              <span class="text-danger">*</span>
            </label>
            <select
              class="form-select"
              id="ease-of-use"
              v-model="survey.easeOfUse"
              :class="{ 'is-invalid': !isFieldValid('easeOfUse') }"
              @change="markFieldAsTouched('easeOfUse')"
            >
              <option value="">Please select</option>
              <option>Very Easy</option>
              <option>Easy</option>
              <option>Neutral</option>
              <option>Difficult</option>
              <option>Very Difficult</option>
            </select>
            <div v-if="shouldShowError('easeOfUse')" class="invalid-feedback">
              Please select an option
            </div>
          </div>

          <!-- Similar modifications for all other fields -->
          <div class="row my-3">
            <label class="form-label" for="recommend">
              Would you recommend this tool to others?
              <span class="text-danger">*</span>
            </label>
            <select
              class="form-select"
              id="recommend"
              v-model="survey.recommendation"
              :class="{ 'is-invalid': !isFieldValid('recommendation') }"
              @change="markFieldAsTouched('recommendation')"
            >
              <option value="">Please select</option>
              <option>Definitely Yes</option>
              <option>Yes</option>
              <option>Neutral</option>
              <option>No</option>
              <option>Definitely No</option>
            </select>
            <div v-if="shouldShowError('recommendation')" class="invalid-feedback">
              Please select an option
            </div>
          </div>

          <!-- Section 2: Prior Experience -->
          <h2 class="text-center">Prior Experience</h2>
          <div class="row my-3">
            <label class="form-label" for="familiarity">
              How familiar are you with FAIR data principles?
              <span class="text-danger">*</span>
            </label>
            <select
              class="form-select"
              id="familiarity"
              v-model="survey.fairFamiliarity"
              :class="{ 'is-invalid': !isFieldValid('fairFamiliarity') }"
              @change="markFieldAsTouched('fairFamiliarity')"
            >
              <option value="">Please select</option>
              <option>Fairly Familiar</option>
              <option>Somewhat Familiar</option>
              <option>Unfamiliar</option>
            </select>
            <div v-if="shouldShowError('fairFamiliarity')" class="invalid-feedback">
              Please select an option
            </div>
          </div>

          <div class="row my-3">
            <label class="form-label" for="prior-usage">
              Have you used other FAIR assessment tools before?
              <span class="text-danger">*</span>
            </label>
            <select
              class="form-select"
              id="prior-usage"
              v-model="survey.priorUsage"
              :class="{ 'is-invalid': !isFieldValid('priorUsage') }"
              @change="markFieldAsTouched('priorUsage')"
            >
              <option value="">Please select</option>
              <option>Yes, frequently</option>
              <option>Yes, occasionally</option>
              <option>No</option>
            </select>
            <div v-if="shouldShowError('priorUsage')" class="invalid-feedback">
              Please select an option
            </div>
          </div>

          <!-- Conditional field for prior tools -->
          <div class="row my-3" v-if="survey.priorUsage.includes('Yes')">
            <label class="form-label" for="prior-tools">
              Which FAIR assessment tools have you used?
              <span class="text-danger">*</span>
            </label>
            <input
              type="text"
              class="form-control"
              id="prior-tools"
              v-model="survey.priorTools"
              :class="{ 'is-invalid': !isFieldValid('priorTools') }"
              @input="markFieldAsTouched('priorTools')"
              style="width: 60%"
              placeholder="Please list the tools you've used separated by comma"
            />
            <div v-if="shouldShowError('priorTools')" class="invalid-feedback">
              Please list the tools you've used
            </div>
          </div>

          <div class="row my-3">
            <label class="form-label" for="prof-status">
              What is your Professions Status?
              <span class="text-danger">*</span>
            </label>
            <select
              class="form-select"
              id="prof-status"
              v-model="survey.professionalStatus"
              :class="{ 'is-invalid': !isFieldValid('professionalStatus') }"
              @change="markFieldAsTouched('professionalStatus')"
            >
              <option value="">Please select</option>
              <option>Student</option>
              <option>Professor</option>
              <option>Researcher</option>
              <option>Other</option>
            </select>
            <div v-if="shouldShowError('professionalStatus')" class="invalid-feedback">
              Please select an option
            </div>
          </div>

          <div class="row my-3">
            <label class="form-label" for="acad-bg">
              What is your Academic Background?
              <span class="text-danger">*</span>
            </label>
            <select
              class="form-select"
              id="acad-bg"
              v-model="survey.academicBG"
              :class="{ 'is-invalid': !isFieldValid('academicBG') }"
              @change="markFieldAsTouched('academicBG')"
            >
              <option value="">Please select</option>
              <option>Computer Sciences/ IT</option>
              <option>Natural Sciences</option>
              <option>Medical Sciences</option>
              <option>Earth & Environmental Sciences</option>
              <option>Agricultural Sciences</option>
              <option>Humanities</option>
              <option>Other</option>
            </select>
            <div v-if="shouldShowError('academicBG')" class="invalid-feedback">
              Please select an option
            </div>
          </div>

          <!-- Conditional field for other academic background -->
          <div class="row my-3" v-if="survey.academicBG.includes('Other')">
            <label class="form-label" for="acad-bg-other">
              Please specify what is your academic background?
              <span class="text-danger">*</span>
            </label>
            <input
              type="text"
              id="acad-bg-other"
              class="form-control"
              v-model="survey.academicBgOther"
              :class="{ 'is-invalid': !isFieldValid('academicBgOther') }"
              @input="markFieldAsTouched('academicBgOther')"
              style="width: 60%"
              placeholder=""
            />
            <div v-if="shouldShowError('academicBgOther')" class="invalid-feedback">
              Please specify your academic background
            </div>
          </div>

          <!-- Section 3: Tool Usefulness -->
          <h2 class="text-center">Tool Usefulness</h2>
          <div class="row my-3">
            <label class="form-label" for="usefulness">
              How useful did you find the tool for FAIR assessment of your datasets?
              <span class="text-danger">*</span>
            </label>
            <select
              class="form-select"
              id="usefulness"
              v-model="survey.usefulness"
              :class="{ 'is-invalid': !isFieldValid('usefulness') }"
              @change="markFieldAsTouched('usefulness')"
            >
              <option value="">Please select</option>
              <option>Extremely Useful</option>
              <option>Very Useful</option>
              <option>Neutral</option>
              <option>Slightly Useful</option>
              <option>Not Useful</option>
            </select>
            <div v-if="shouldShowError('usefulness')" class="invalid-feedback">
              Please select an option
            </div>
          </div>

          <div class="row my-4">
            <label class="form-label" for="slider">
              How effective do you think the tool is in assessing FAIR data? Please Rate out of 10
              <span class="text-danger">*</span>
            </label>
            <div class="slider-container">
              <span
                class="badge rounded-pill bg-primary bubble position-absolute"
                :style="{ left: ((survey.fairRating - 0) * 100) / 10 + '%' }"
              >
                {{ survey.fairRating }}
              </span>
              <div class="input-group">
                <input
                  type="range"
                  id="slider"
                  class="form-range"
                  :class="{ 'is-invalid': !isFieldValid('fairRating') }"
                  min="0"
                  max="10"
                  step="1"
                  v-model="survey.fairRating"
                  @input="markFieldAsTouched('fairRating')"
                />
              </div>
              <div v-if="shouldShowError('fairRating')" class="invalid-feedback">
                Please select a rating
              </div>
            </div>
          </div>

          <div class="row my-3">
            <label class="form-label" for="useful-aspect">
              Which type of Assessment(s) have you tried with the Tool?
              <span class="text-danger">*</span>
            </label>
            <select
              class="form-select"
              id="useful-aspect"
              v-model="survey.usefulAspects"
              :class="{ 'is-invalid': !isFieldValid('usefulAspects') }"
              @change="markFieldAsTouched('usefulAspects')"
            >
              <option value="">Please select</option>
              <option>Online</option>
              <option>Offline</option>
              <option>Both</option>
            </select>
            <div v-if="shouldShowError('usefulAspects')" class="invalid-feedback">
              Please select an option
            </div>
          </div>

          <div class="row my-3">
            <label class="form-label" for="future-use">
              How likely are you to use this tool in the future?
              <span class="text-danger">*</span>
            </label>
            <select
              class="form-select"
              id="future-use"
              v-model="survey.futureUsage"
              :class="{ 'is-invalid': !isFieldValid('futureUsage') }"
              @change="markFieldAsTouched('futureUsage')"
            >
              <option value="">Please select</option>
              <option>Very Likely</option>
              <option>Likely</option>
              <option>Unlikely</option>
              <option>Very Unlikely</option>
            </select>
            <div v-if="shouldShowError('futureUsage')" class="invalid-feedback">
              Please select an option
            </div>
          </div>

          <!-- Additional Comments -->
          <h2 class="text-center">Additional Comments</h2>
          <div class="row my-3 justify-content-center">
            <textarea
              class="form-control"
              id="more-comments"
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
  font-size: 3em;
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
  padding-top: 2rem;
  padding-bottom: 1rem;
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

.fs-6 {
  font-size: 0.98rem !important;
}

.text-muted {
  color: #6c757d !important;
}

/* Add styles for invalid fields */
.is-invalid {
  border-color: #dc3545 !important;
}

.invalid-feedback {
  display: block;
  width: 100%;
  margin-top: 0.25rem;
  font-size: 0.875em;
  color: #dc3545;
}
</style>
