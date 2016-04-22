(function() {
    'use strict';

    angular
        .module('digest')
        .controller('DigestController', DigestController);

    /** @ngInject */
    DigestController.$inject = ['entryModel', 'categoryModel'];

    function DigestController(entryModel, categoryModel) {
        var vm = this;

        vm.getAllEntries = getAllEntries;
        vm.getAllCategories = getAllCategories;
        vm.filterEntries = filterEntries;
        vm.filterCategories = filterCategories;
        vm.sendReport = sendReport;
        vm.searchTextChange = searchTextChange;
        vm.entries = [];
        vm.categories = [];
        vm.fromDate = null;
        vm.toDate = null;
        vm.email = null;
        vm.selectedCategory = null;

        init();

        function getAllEntries() {
            entryModel.getAll()
                .then(function (entries) {
                    vm.entries = entries;
                }, function (err) {
                    alert(err);   // a modal pop up should be used instead of alert
                })
        }

        function getAllCategories() {
            categoryModel.getAll()
                .then(function (categories) {
                    vm.categories = categories;
                }, function (err) {
                    alert(err);   // a modal pop up should be used instead of alert
                })
        }

        function init() {
            getAllEntries();
            getAllCategories();
        }

        function filterEntries() {
            if (vm.selectedCategory == null){
                entryModel.filter(vm.fromDate, vm.toDate, null)
                    .then(function (response) {
                        vm.entries = response.entries;
                    }, function (err) {
                        alert(err);
                    });
            }else{
                entryModel.filter(vm.fromDate, vm.toDate, vm.selectedCategory.pk)
                    .then(function (response) {
                        vm.entries = response.entries;
                    }, function (err) {
                        alert(err);
                    });
            }
        }

        function filterCategories(searchText) {
            categoryModel.filter(searchText)
                .then(function (response) {
                    vm.categories = response;
                }, function (err) {
                    alert(err);
                })
        }

        function searchTextChange(searchText) {
            filterCategories(searchText);
        }

        function sendReport() {
            if (vm.email == null){
                alert("Please type your email");
                return;
            }

            var ids = getEntryIds();
            entryModel.report(vm.email, ids)
                .then(function (response) {
                    alert("Sent to your email");
                }, function (err) {
                    alert(err.message);
                })
        }

        function getEntryIds() {
            var ids = [];
            vm.entries.forEach(function (entry) {
                ids.push(entry.pk);
            });
            return ids;
        }
    }
})();