package org.eclipse.tracecompass.internal.lttng2.kernel.segment.analysis;
//package org.eclipse.tracecompass.internal.lttng2.kernel.core.segment.analysis;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.Collection;

import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.jdt.annotation.NonNull;
import org.eclipse.tracecompass.analysis.os.linux.core.latency.SystemCallLatencyAnalysis;
import org.eclipse.tracecompass.analysis.timing.core.segmentstore.AbstractSegmentStoreAnalysisModule;
import org.eclipse.tracecompass.segmentstore.core.ISegment;
import org.eclipse.tracecompass.segmentstore.core.ISegmentStore;
import org.eclipse.tracecompass.segmentstore.core.treemap.TreeMapStore;
import org.eclipse.tracecompass.tmf.core.exceptions.TmfAnalysisException;
import org.eclipse.tracecompass.tmf.core.trace.ITmfTrace;
import org.eclipse.tracecompass.tmf.core.trace.TmfTraceManager;
import org.eclipse.tracecompass.tmf.core.trace.TmfTraceUtils;
//import org.eclipse.tracecompass.tmf.core.trace.ITmfTrace;
//import org.eclipse.tracecompass.tmf.core.trace.TmfTraceManager;

/**
 * @since 2.0
 */
public class FrankSegmentComparator extends AbstractSegmentStoreAnalysisModule {//extends TmfAbstractAnalysisModule {

    /**
     * ID
     */
    public static final String ID = "org.eclipse.tracecompass.internal.lttng2.kernel.segment.analysis.FrankSegmentComparator"; //$NON-NLS-1$

    /**
     * @param list_x
     */
    protected void make_straight_comparison(ArrayList<ISegmentStore<@NonNull ISegment>> list){
        System.out.println("make_straight_comparison");
        //list to get first and second argument:
        boolean empty = list.isEmpty();

        ISegmentStore<@NonNull ISegment> first_storage = list.get(0);
        ISegmentStore<@NonNull ISegment> second_storage = list.get(1);

        System.out.println("make_straight_comparison is it empty?" + empty);

        System.out.println("Are they straight equal?" + first_storage.equals(second_storage));
       //Straight comparison
        for ( @NonNull ISegmentStore<@NonNull ISegment> store: list)
        {
            //element.equals();

            System.out.println(store.size());
            for ( @NonNull ISegment element: store)
            {
                System.out.println(element);
            }
        }
        //if(size1 == size2)
        //    System.out.println("Their sizes are equal");

        return;
    }

    /*Comparision 2*/
    protected void make_windows_folding_comparison(ArrayList<ISegmentStore<@NonNull ISegment>> list){
        System.out.println("make_windows_folding_comparison");
        //list to get first and second argument:
        boolean empty = list.isEmpty();

        ISegmentStore<@NonNull ISegment> first_storage = list.get(0);
        ISegmentStore<@NonNull ISegment> second_storage = list.get(1);

        //ISegment[3] Vetor = null;
        //Put in Segment Storage

        System.out.println("Are they straight equal?" + first_storage.equals(second_storage));
       //Straight comparison
        for ( @NonNull ISegmentStore<@NonNull ISegment> store: list)
        {
            //element.equals();

            System.out.println(store.size());
            for ( @NonNull ISegment element: store)
            {
                System.out.println(element);
            }
        }

        //if(size1 == size2)
        //    System.out.println("Their sizes are equal");

        return; //return the comparision table
    }
    /*Comparison 3*/
    protected void make_correlation_comparison(ArrayList<ISegmentStore<@NonNull ISegment>> list_x){
        System.out.println("make_windows_folding_comparison");
        //list to get first and second argument:
        boolean empty = list_x.isEmpty();

        //ISegmentStore<@NonNull ISegment> second = list_x.get(1);
        int correlation_index = 3;

        System.out.println("make_straight_comparison 2" + empty + correlation_index);
        /*for ( @NonNull ISegment element: first)
        {
            //Make the correlation


        }*/

        return; //return correlation table
    }

    /*Comparision 3*/
    protected void make_abstraction_comparison(ArrayList<ISegmentStore<@NonNull ISegment>> list_x){
        System.out.println("make_windows_folding_comparison");
        //list to get first and second argument:
        boolean empty = list_x.isEmpty();

        //ISegmentStore<@NonNull ISegment> second = list_x.get(1);
        int abstraction_index = 3;

        System.out.println("make_straight_comparison 2" + abstraction_index + empty);
        /*for ( @NonNull ISegment element: first)
        {

        }*/

        return;
    }

    @Override
    protected void canceling() {
        // TODO Auto-generated method stub

    }
    @Override
    protected Object @NonNull [] readObject(@NonNull ObjectInputStream ois) throws ClassNotFoundException, IOException {
        // TODO Auto-generated method stub
        return null;
    }
    @Override
    protected boolean buildAnalysisSegments(@NonNull ISegmentStore<@NonNull ISegment> segmentStore, @NonNull IProgressMonitor monitor) throws TmfAnalysisException {

            System.out.println("executeAnalysis"); //$NON-NLS-1$
            ITmfTrace trace = getTrace();
            int i = 0;
            //@NonNull
            Collection<@NonNull ITmfTrace> traceSet = TmfTraceManager.getTraceSet(trace);
            System.out.println(traceSet.isEmpty());
            //@Nullable
            ISegmentStore<@NonNull ISegment> sumResult =  new TreeMapStore<>();

            //Array:
            ArrayList<ISegmentStore<@NonNull ISegment>> list_segments = new ArrayList<>();
            //eachResult:
            ISegmentStore<@NonNull ISegment> eachResult;
            //SystemCallLatency:
            SystemCallLatencyAnalysis eachSystemCall;

            for (ITmfTrace t: traceSet)
            {
                //TmfTraceUtils.getAnalysisModuleOfClass(
                System.out.println(t.toString());
                eachSystemCall = TmfTraceUtils.getAnalysisModuleOfClass(t, SystemCallLatencyAnalysis.class, SystemCallLatencyAnalysis.ID);

                //eachSystemCall = TmfTraceUtils.getAnalysisModuleOfClass(t, SystemCallLatencyAnalysis.class, SystemCallLatencyAnalysis.ID);
                if(eachSystemCall == null) {
                    System.out.println("break");
                    break;
                }

                eachSystemCall.schedule();
                eachSystemCall.waitForCompletion();
                eachResult = eachSystemCall.getSegmentStore();

                if(eachResult != null) {
                    System.out.println("Each result");
                    sumResult.addAll(eachResult);//(ISegmentStore) eachResult);
                    list_segments.add(eachResult);
                }
                else{
                    System.out.println("empty");
                }
            }

            //Send the first and second for the view:
            //list_segments.get(0);
            //list_segments.get(1);
            make_straight_comparison(list_segments);

            if(i <1) {
                return false;
            }

        return false;
    }

}

