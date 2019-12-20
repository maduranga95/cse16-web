<template>
    <div class="row">
        <div class="col m3 l3"></div>
        <div v-if="!photoURL || !name || !id">
            <div class="progress">
                <div class="indeterminate"></div>
            </div>
        </div>
        <div v-else class="col s12 m6 l6">
            <div class="card">
                <div class="card-image">
                    <img src="../../assets/batch16.jpg">
                    <a class="btn-floating halfway-fab waves-effect waves-light profile-btn left"><img :src="photoURL"/></a>
                </div>
                <div class="card-content">
                    <span class="card-title">{{ name }} ({{ id }})</span>
                    <h6>C-GPA: {{ cgpa }}</h6>
                    <h6>C-Rank: {{ crank }}</h6>
                </div>
            </div>
        </div>
        <div class="col m3 l3"></div>
    </div>
</template>

<script>
    import firebase from 'firebase'
    import db from '@/firebase/init'
    export default {
        name: 'Profile',
        data() {
            return {
                cgpa: null,
                crank: null,
                email: null,
                field: null,
                id: null,
                mobile: null,
                name: null,   
                photoURL: null    
            }
        },
        created() {
            this.email = firebase.auth().currentUser.email
            this.photoURL = firebase.auth().currentUser.photoURL
            if(!this.photoURL) {
                this.photoURL = require('../../assets/user.jpg')
            }
            db.collection("students").doc(this.email).get().then(doc => {
                this.cgpa = doc.data().cgpa
                this.crank = doc.data().crank
                this.field = doc.data().field
                this.id = doc.data().id
                this.mobile = doc.data().mobile
                this.name = doc.data().name
            })
        },
    }
</script>

<style>
    .profile-btn {
        width: 20%;
        height: auto;
        border: 2px solid #fff;
    }
</style>