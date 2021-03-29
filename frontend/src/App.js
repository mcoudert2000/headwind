import React, {useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import $ from 'jquery';

const useStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      margin: theme.spacing(1),
    },
  },
  input: {
    display: 'none',
  },
}));



function App() {
	const [selectedFile, setSelectedFile] = useState();
	const [isSelected, setIsSelected] = useState(false);
  const [map, setMap] = useState();
  const classes = useStyles();

	const changeHandler = (event) => {
		setSelectedFile(event.target.files[0]);
		setIsSelected(true);
	};

	const handleSubmission = () => {
		const formData = new FormData();

		formData.append('file', selectedFile);

		fetch(
			'upload',
			{
				method: 'POST',
				body: formData,
			}
		)
			.then((response) => response.json())
			.then((result) => {
				console.log('Success:', result.html);
        setMap(result.html);
			})
			.catch((error) => {
				console.error('Error:', error);
			});
	};
  console.log(map);
	return(
   <div>
			<input 
        type="file" 
        name="file" 
        id="gpx-uploader"
        accept=".gpx" 
        onChange={changeHandler} 
      />
			{isSelected ? (
				<div>
					<p>Filename: {selectedFile.name}</p>
					<p>Size in bytes: {selectedFile.size}</p>
					<p>
						lastModifiedDate:{' '}
						{selectedFile.lastModifiedDate.toLocaleDateString()}
					</p>
				</div>
			) : (
				<p>Select a file</p>
			)}
			<div>
				<button onClick={handleSubmission}>Submit</button>
			</div>
      {map && 
       <div dangerouslySetInnerHTML={{__html: map }} />}
		</div>
	);
}


// function App() {
//   const classes = useStyles();

//   function sendData(data) {
//     console.log(data.files);
//     let toRequest = {
//       url: "localhost:5000/upload",
//       type: "POST",
//       success: () => {
//         console.log('yay');
//       },
//       error: () => {
//         console.log('problem');
//       }, 
//       data: data.files[0]
//     };
//     $.
//   }

//   return (
//     <div className={classes.root}>
//       <form onSubmit={sendData}>
//         <input
//           accept=".gpx"
//           className={classes.input}
//           id="gpx-uploader"
//           type="file"
//         />
//         <label htmlFor="gpx-uploader">
//           <Button variant="contained" color="primary" component="span">
//             Upload
//           </Button>
//         </label>
//         <Button variant="contained" color="primary" component="span" type="submit">
//           Submit
//         </Button>
//       </form>
//     </div>
//   );
// }

/* <div className={classes.root}>
      <input
        accept=".gpx"
        className={classes.input}
        id="contained-button-file"
        multiple
        type="file"
      />
      <label htmlFor="contained-button-file">
        <Button
          variant="contained"
          color="default"
          className={classes.button}
          startIcon={<CloudUploadIcon />}
        >
          Upload
        </Button>
      </label>
    </div> */

export default App;
