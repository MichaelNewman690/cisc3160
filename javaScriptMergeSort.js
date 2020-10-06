console.clear();
const someArray=[35, 16, 22, 18, 91, 108, 5, 4, 3, 2, 1];
mergeSort(someArray, 0, someArray.length-1);
console.log(someArray);



function mergeSort(arr, left, right){
  if(left < right){
    const middle = Math.floor((left+right)/2);

    mergeSort(arr, left, middle);
    mergeSort(arr, middle+1, right);

    merge(arr, left, middle, right);
  }
}

function merge(arr, left, middle, right){
  const tempLeft = [];
  const tempRight = [];

  for(let i=left; i <= middle; i++){
    tempLeft.push(arr[i]);
  }
  for(let i=middle+1; i <= right; i++){
    tempRight.push(arr[i]);

  }
  console.log(tempLeft);
  console.log(tempRight);
  const leftLength = tempLeft.length;
  const rightLength = tempRight.length;
  let leftPlace = 0;
  let rightPlace = 0;
  let place = left;

  while(leftPlace < leftLength && rightPlace < rightLength){
    if(tempLeft[leftPlace] <= tempRight[rightPlace]){
      arr[place++]=tempLeft[leftPlace++];
    }
    else{
      arr[place++]=tempRight[rightPlace++];
    }
  }

  if(leftPlace < leftLength){
    for(leftPlace; leftPlace < leftLength; leftPlace++){
      arr[place++]=tempLeft[leftPlace];
    }
  }
  else if(rightPlace < rightLength){
    for(rightPlace; rightPlace < rightLength; rightPlace++){
      arr[place++]=tempRight[rightPlace];
    }
  }
}
